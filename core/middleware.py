from django.utils.deprecation import MiddlewareMixin
import user_agents 
from core.models import UserAccessLog

class UserAgentMiddleware(MiddlewareMixin):
    def process_request(self, request):
        user_agent_string = request.META.get("HTTP_USER_AGENT", '')
        user_agent = user_agents.parse(user_agent_string)
        request.user_os = user_agent.os.family 
        
        UserAccessLog.objects.create(
            user = request.user if request.user.is_authenticated else None,
            os = request.user_os,
            path = request.path,
            ip = request.META.get('REMOTE_ADDR')
        )
