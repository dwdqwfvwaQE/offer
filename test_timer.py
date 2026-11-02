# -*- coding: utf-8 -*-
"""
Тестирование таймера
"""
from datetime import datetime, timedelta, timezone
from database import Offer

# Создаём тестовый оффер
test_offer = Offer(
    id=1,
    business_connection_id="test",
    chat_id=123456,
    source_message_id=1,
    buyer_id=999,
    buyer_name="Иван",
    buyer_username="ivan",
    gift_url="https://t.me/giftcode/test",
    gift_name="Delicious Cake",
    gift_number=1234,
    language="ru",
    amount=1000,
    currency="gram",
    status="pending",
    created_at=datetime.now(timezone.utc),
    expires_at=datetime.now(timezone.utc) + timedelta(hours=6, minutes=30),
    offer_message_id=12345,
)

# Импортируем функции
import sys
sys.path.insert(0, '.')
from bot import remaining_time_text, timer_text, offer_caption

print("=== Тест таймера ===\n")

print(f"Оставшееся время: {remaining_time_text(test_offer)}")
print(f"Таймер текст: {timer_text(test_offer)}")
print()

print("=== Полный caption оффера ===")
print(offer_caption(test_offer))
print()

# Тестируем с почти истёкшим временем
test_offer_expiring = Offer(
    id=2,
    business_connection_id="test",
    chat_id=123456,
    source_message_id=2,
    buyer_id=999,
    buyer_name="Пётр",
    buyer_username="petr",
    gift_url="https://t.me/giftcode/test2",
    gift_name="Golden Star",
    gift_number=5678,
    language="ru",
    amount=500,
    currency="stars",
    status="pending",
    created_at=datetime.now(timezone.utc),
    expires_at=datetime.now(timezone.utc) + timedelta(minutes=15),
    offer_message_id=12346,
)

print("=== Тест с истекающим оффером (15 минут) ===")
print(offer_caption(test_offer_expiring))
