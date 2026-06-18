"""Shared orchestration v1 helper used by lessons 2–6."""

from __future__ import annotations

from gen_ai_hub.orchestration.models.config import OrchestrationConfig
from gen_ai_hub.orchestration.models.llm import LLM
from gen_ai_hub.orchestration.models.template import TemplateValue
from gen_ai_hub.orchestration.service import OrchestrationService
from gen_ai_hub.proxy import get_proxy_client

from .orchestration_helper import get_orchestration_deployment_url

_proxy_client = None
_orchestration_service = None
_deployment_url = None


def init_orchestration_service(
    api_url: str | None = None,
    default_model: str = "meta--llama3.1-70b-instruct",
):
    global _proxy_client, _orchestration_service, _deployment_url
    _proxy_client = get_proxy_client()
    _deployment_url = api_url or get_orchestration_deployment_url(_proxy_client.ai_core_client)
    _orchestration_service = OrchestrationService(
        api_url=_deployment_url,
        proxy_client=_proxy_client,
    )
    return _orchestration_service, default_model


def send_request(
    prompt,
    _print: bool = True,
    _model: str = "meta--llama3.1-70b-instruct",
    **kwargs,
) -> str:
    if _orchestration_service is None:
        init_orchestration_service(default_model=_model)

    config = OrchestrationConfig(
        llm=LLM(name=_model),
        template=prompt,
    )
    template_values = [TemplateValue(name=key, value=value) for key, value in kwargs.items()]
    answer = _orchestration_service.run(config=config, template_values=template_values)
    result = answer.module_results.llm.choices[0].message.content

    if _print:
        formatted_prompt = "\n".join(t.content for t in answer.module_results.templating)
        print(f"<-- PROMPT --->\n{formatted_prompt}\n<--- RESPONSE --->\n{result}")

    return result
