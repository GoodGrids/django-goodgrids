import logging

from django.http import HttpResponse
from django_goodgrids.goodgrids import convert_to_excel_file

logger = logging.getLogger(__name__)


class GoodGridsExcelExportViewMixin(object):
    good_grids_api_url = None
    excel_file_name = None

    def get_goodgrids_api_url(self):
        if not self.good_grids_api_url:
            raise RuntimeError('Define the good_grids_api_url property or override get_goodgrids_api_url()')
        return self.good_grids_api_url

    def get_excel_file_name(self):
        if not self.excel_file_name:
            raise RuntimeError('Define the excel_file_name property or override get_excel_file_name()')
        return self.excel_file_name

    def dispatch(self, request, *args, **kwargs):
        """
        Assumes that the parent class's dispatch method return an HttpResponse containing a CSV file.
        Converts that CSV file to an Excel file using the GoodGrids API.
        If it fails, it returns the original CSV file.
        """
        csv_response = super(GoodGridsExcelExportViewMixin, self).dispatch(request, *args, **kwargs)
        try:
            excel_file = convert_to_excel_file(csv_response.content, self.get_goodgrids_api_url())

            response = HttpResponse(
                excel_file, content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
            response['Content-Disposition'] = 'filename={}'.format(self.get_excel_file_name())

            return response
        except RuntimeError as x:
            # In case Excel download fails, return the CSV file
            logger.exception(x)
            return csv_response


def create_goodgrids_excel_export_view(csv_export_view, goodgrids_api_url, excel_file_name):
    def goodgrids_excel_export_view(request):
        csv_response = csv_export_view(request)

        csv_content = csv_response.content
        excel_file = convert_to_excel_file(csv_content, goodgrids_api_url)

        response = HttpResponse(
            excel_file,
            content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
        response['Content-Disposition'] = 'filename={}'.format(excel_file_name)

        return response

    return goodgrids_excel_export_view
