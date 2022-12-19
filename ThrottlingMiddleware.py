
from aiogram import Dispatcher
from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.dispatcher import DEFAULT_RATE_LIMIT
from aiogram.dispatcher.handler import CancelHandler, current_handler
from aiogram.utils.exceptions import Throttled
import asyncio
from typing import Union

class ThrottlingMiddleware(BaseMiddleware):

    def __init__(self, limit=DEFAULT_RATE_LIMIT, key_prefix='antiflood_'):
        self.rate_limit = limit
        self.prefix = key_prefix
        super(ThrottlingMiddleware, self).__init__()

    async def throttle(self, target: Union[types.Message, types.CallbackQuery]):
        handler = current_handler.get()
        dispatcher = Dispatcher.get_current()
        if not handler:
            return
        limit = getattr(handler, 'throttling_rate_limit', self.rate_limit)
        key = getattr(handler, 'throttling_key', f"{self.prefix}_{handler.__name__}")

        try:
            await dispatcher.throttle(key, rate=limit)
        except Throttled as t:
            await self.target_throttled(target, t, dispatcher, key)
            raise CancelHandler()

    @staticmethod
    async def target_throttled(target: Union[types.Message, types.CallbackQuery],
                               throttled: Throttled, dispatcher: Dispatcher, key: str):
        msg = target.message if isinstance(target, types.CallbackQuery) else target
        delta = throttled.rate - throttled.delta

        await asyncio.sleep(delta)

        if throttled.exceeded_count == 2:
            await msg.reply('Слишком Часто! Давай не так быстро')
            return
        elif throttled.exceeded_count == 3:
            await msg.reply(f'⚠ Хватит!')
            return
        elif throttled.exceeded_count == 4:
            await msg.reply(f'⚠ Я тебя по IP вычислю!!!')
            return
        elif throttled.exceeded_count == 5:
            await msg.reply(f'⚠ Теперь, тебе придётся чутка подождать))0)')
            return

    async def on_process_message(self, message, data):
        await self.throttle(message)

    async def on_process_callback_query(self, call, data):
        await self.throttle(call)
def rate_limit(limit: float, key=None):
    def decorator(func):
        setattr(func, "throttling_rate_limit", limit)
        if key:
            setattr(func, "throttling_key", key)
        return func

    return decorator


