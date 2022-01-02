from rest_framework.decorators import api_view

from django.http import JsonResponse

from ..models.const import OhshownEventConst

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


@swagger_auto_schema(
    method="get",
    operation_summary="Get Ohshown event type list",
    responses={200: openapi.Response("results", openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "value": openapi.Schema(type=openapi.TYPE_STRING, description="Ohshown event type value"),
            "text": openapi.Schema(type=openapi.TYPE_STRING, description="Ohshown event type text")
        },
    )), 400: "request failed"},
)
@api_view(["GET"])
def get_ohshown_event_type_list(request):
    return JsonResponse(_to_value_and_text_format(OhshownEventConst.TYPE_LIST), safe=False)


def _to_value_and_text_format(resource_tuple_list):
    return [{"value": resource_tuple[0], "text": resource_tuple[1]} for resource_tuple in resource_tuple_list]
