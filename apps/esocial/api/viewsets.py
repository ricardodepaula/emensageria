from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
import json

from django.shortcuts import redirect, get_object_or_404, render

from django.forms.models import model_to_dict
from .serializers import EventosSerializer
from ..models import Eventos
from ..choices import EVENTO_ORIGEM_API


class EventosViewSet(ModelViewSet):
    queryset = Eventos.objects.all()
    serializer_class = EventosSerializer
    # filterset_class = EventosFilter
    http_method_names = ['get', 'put', 'patch', 'post', 'head', 'delete']
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        filter = {}
        if self.request.query_params.get('user_id'):
            filter['created_by_id'] = int(self.request.query_params.get('user_id'))
        if self.request.query_params.get('identidade'):
            filter['identidade'] = self.request.query_params.get('identidade')
        return Eventos.objects.filter(**filter).all()

    @action(detail=True, methods=['get'], url_path='atualizar-identidade')
    def atualizar_identidade(self, request, pk=None):
        obj = get_object_or_404(Eventos, id=pk)
        obj.make_identidade()
        return Response(
            {'id': obj.id,
             'identidade': obj.identidade, })

    @action(detail=True, methods=['get'], url_path='abrir-evento-para-edicao')
    def abrir_evento_para_edicao(self, request, pk=None):
        obj = get_object_or_404(Eventos, id=pk)
        obj.abrir_evento_para_edicao()
        return Response(
            {'id': obj.id,
             'identidade': obj.identidade,
             'status': obj.status,
             'status_txt': obj.get_status_display(), })

    @action(detail=True, methods=['get'], url_path='validar')
    def validar(self, request, pk=None):
        obj = get_object_or_404(Eventos, id=pk)
        if not obj.transmissor_evento:
            obj.vincular_transmissor()
        obj.create_xml()
        obj.validar()
        obj = get_object_or_404(Eventos, id=pk)
        return Response(
            {'id': obj.id,
             'identidade': obj.identidade,
             'status': obj.status,
             'status_txt': obj.get_status_display(),
             'ocorrencias': json.loads(obj.ocorrencias_json or '{}'), })

    @action(detail=True, methods=['get'], url_path='enviar')
    def enviar(self, request, pk=None):
        from ..choices import STATUS_EVENTO_AGUARD_ENVIO, STATUS_EVENTO_IMPORTADO
        obj = get_object_or_404(Eventos, id=pk)

        if obj.status in [STATUS_EVENTO_AGUARD_ENVIO, STATUS_EVENTO_IMPORTADO]:
            retorno = obj.enviar()
            dic = {'id': obj.id,
                 'identidade': obj.identidade,
                 'status': obj.status,
                 'status_txt': obj.get_status_display(),
                 'ocorrencias': json.loads(obj.ocorrencias_json or '{}'), }
            retorno.update(dic)
            obj = get_object_or_404(Eventos, id=pk)
            return Response({'id': obj.id,
                 'retorno': retorno.get('retorno'),
                 'mensagem': retorno.get('mensagem'),
                 'identidade': obj.identidade,
                 'status': obj.status,
                 'status_txt': obj.get_status_display(),
                 'ocorrencias': json.loads(obj.ocorrencias_json or '{}'),
                 'retorno_envio': json.loads(obj.retorno_envio_json or '{}'),
                 'retorno_envio_lote': retorno.get('retorno_envio'), })
        else:
            return Response({'retorno': 'error',
                    'mensagem': 'Não foi possivel enviar o evento, pois somente poderá ser enviado com os status "Aguardando envio" ou "Importado"'})

    @action(detail=True, methods=['get'], url_path='consultar')
    def consultar(self, request, pk=None):
        from ..choices import STATUS_EVENTO_ENVIADO, STATUS_EVENTO_PROCESSADO
        obj = get_object_or_404(Eventos, id=pk)
        if obj.status in [STATUS_EVENTO_ENVIADO, STATUS_EVENTO_PROCESSADO]:
            retorno = obj.consultar()
            dic = {'id': obj.id,
                 'identidade': obj.identidade,
                 'status': obj.status,
                 'status_txt': obj.get_status_display(),
                 'ocorrencias': json.loads(obj.ocorrencias_json or '{}'), }
            retorno.update(dic)
            obj = get_object_or_404(Eventos, id=pk)
            return Response({'id': obj.id,
                 'retorno': retorno.get('retorno'),
                 'mensagem': retorno.get('mensagem'),
                 'identidade': obj.identidade,
                 'status': obj.status,
                 'status_txt': obj.get_status_display(),
                 'ocorrencias': json.loads(obj.ocorrencias_json or '{}'),
                 'retorno_consulta': json.loads(obj.retorno_consulta_json or '{}'),
                 'retorno_consulta_lote': retorno.get('retorno_consulta'), })
        else:
            return Response({'retorno': 'error',
                    'mensagem': 'Não foi possivel consultar o evento, pois o mesmo somente poderá ser consultado caso esteja com os status "Enviado" ou "Consultado"'})
