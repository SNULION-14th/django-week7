from django.contrib.auth.hashers import make_password
from django.db import migrations


def seed_dummy_data(apps, schema_editor):
    Language = apps.get_model("post", "Language")
    AppUser = apps.get_model("post", "User")
    ChatRoom = apps.get_model("post", "ChatRoom")
    ChatRoomMember = apps.get_model("post", "ChatRoomMember")
    Message = apps.get_model("post", "Message")
    MessageTranslation = apps.get_model("post", "MessageTranslation")
    AuthUser = apps.get_model("auth", "User")

    Language.objects.update_or_create(
        code="ko",
        defaults={"name": "Korean", "native_name": "한국어"},
    )
    Language.objects.update_or_create(
        code="de",
        defaults={"name": "German", "native_name": "Deutsch"},
    )
    Language.objects.update_or_create(
        code="en",
        defaults={"name": "English", "native_name": "English"},
    )

    minsu, _ = AppUser.objects.update_or_create(
        email="minsu@example.com",
        defaults={
            "password": "sample-password",
            "nickname": "민수",
            "preferred_language_code_id": "ko",
            "profile_image_url": "",
        },
    )
    hans, _ = AppUser.objects.update_or_create(
        email="hans@example.com",
        defaults={
            "password": "sample-password",
            "nickname": "Hans",
            "preferred_language_code_id": "de",
            "profile_image_url": "",
        },
    )

    room, _ = ChatRoom.objects.update_or_create(
        title="민수와 Hans의 번역 채팅",
        defaults={
            "room_type": "DM",
            "created_by": minsu,
        },
    )

    minsu_member, _ = ChatRoomMember.objects.update_or_create(
        chat_room=room,
        user=minsu,
        defaults={
            "display_language_code_id": "ko",
            "left_at": None,
        },
    )
    hans_member, _ = ChatRoomMember.objects.update_or_create(
        chat_room=room,
        user=hans,
        defaults={
            "display_language_code_id": "de",
            "left_at": None,
        },
    )

    minsu_message, _ = Message.objects.update_or_create(
        chat_room=room,
        sender=minsu,
        original_content="안녕! 오늘 독일 날씨 어때?",
        defaults={
            "original_language_code_id": "ko",
            "message_type": "TEXT",
            "deleted_at": None,
        },
    )
    hans_message, _ = Message.objects.update_or_create(
        chat_room=room,
        sender=hans,
        original_content="Guten Morgen! Heute ist das Wetter sehr gut.",
        defaults={
            "original_language_code_id": "de",
            "message_type": "TEXT",
            "deleted_at": None,
        },
    )

    MessageTranslation.objects.update_or_create(
        message=minsu_message,
        target_language_code_id="de",
        defaults={
            "translated_content": "Hallo! Wie ist das Wetter heute in Deutschland?",
            "translation_status": "DONE",
            "provider": "Dummy",
        },
    )
    MessageTranslation.objects.update_or_create(
        message=hans_message,
        target_language_code_id="ko",
        defaults={
            "translated_content": "좋은 아침이야! 오늘 날씨가 아주 좋아.",
            "translation_status": "DONE",
            "provider": "Dummy",
        },
    )

    minsu_member.last_read_message = hans_message
    minsu_member.save(update_fields=["last_read_message"])
    hans_member.last_read_message = minsu_message
    hans_member.save(update_fields=["last_read_message"])

    AuthUser.objects.update_or_create(
        username="admin",
        defaults={
            "email": "admin@example.com",
            "password": make_password("admin1234"),
            "is_staff": True,
            "is_superuser": True,
            "is_active": True,
        },
    )


def remove_dummy_data(apps, schema_editor):
    AuthUser = apps.get_model("auth", "User")
    AppUser = apps.get_model("post", "User")
    Language = apps.get_model("post", "Language")

    AuthUser.objects.filter(username="admin").delete()
    AppUser.objects.filter(email__in=["minsu@example.com", "hans@example.com"]).delete()
    Language.objects.filter(code__in=["ko", "de", "en"]).delete()


class Migration(migrations.Migration):
    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
        ("post", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(seed_dummy_data, remove_dummy_data),
    ]
