from django.shortcuts import render, HttpResponse
from django.views import View
from bot.agent.wagent import query_agent
import asyncio

# Create your views here.
class BotView(View):
    async def post(self, request):
        user_message = request.POST.get('message', '')
        if not user_message:
            context = {
                'bot_response': 'Please enter a weather related message to get a response.',
            }
            return render(request, 'main.html', context)
        try:
            bot_response = await query_agent(user_message)
        except Exception as e:
            bot_response = f"An error occurred: {str(e)}"
        context = {
            'user_message': user_message,
            'bot_response': bot_response,
        }
        return render(request, 'main.html', context)

