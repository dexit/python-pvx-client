import base64

import zeep


class PvxClient(object):

    WSDL_URL = 'http://wms.peoplevox.net/{0}/resources/integrationservicev4.asmx?wsdl'

    def __init__(self, client_id, username, password):
        client = zeep.Client(wsdl=self.WSDL_URL.format(client_id), strict=False)
        auth_response = client.service.Authenticate(client_id,
                                                    username,
                                                    base64.b64encode(password))
        session = auth_response['Detail'].split(',')[1]
        SessionCredentials = client.get_type('ns0:UserSessionCredentials')
        creds = SessionCredentials(UserId=0, ClientId=client_id, SessionId=session)
        self._client = client
        self._auth = {'_soapheaders': [creds]}

    def get_report(self, report_name, columns, sort=None, filters=None, page_num=1, page_size=0):
        GetReportRequest = self._client.get_type('ns0:GetReportRequest')
        get_report_request = GetReportRequest(
            TemplateName=report_name,
            PageNo=page_num,
            ItemsPerPage=page_size,
            OrderBy=sort,
            Columns=columns,
            SearchClause=filters
        )
        report = self._client.service.GetReportData(
            getReportRequest=get_report_request,
            **self._auth
        )
        return report