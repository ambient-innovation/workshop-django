class SessionService:
    SESSION_LAST_SET_DUT_COMPANY_ID = 'last_set_dut_company_id'
    SESSION_LAST_SET_DUT_CATEGORY_ID = 'last_set_dut_category_id'
    SESSION_LAST_SET_DUT_LOCATION_ID = 'last_set_dut_location_id'

    SESSION_LAST_SET_TEMPLATE_COMPANY_ID = 'last_set_template_company_id'
    SESSION_LAST_SET_TEMPLATE_INSPECTION_TYPE_ID = 'last_set_template_inspection_type_id'

    '''
    DUT
    '''

    @staticmethod
    def get_last_set_dut_company_id(request) -> int:
        return request.session.get(SessionService.SESSION_LAST_SET_DUT_COMPANY_ID, None)

    @staticmethod
    def set_last_set_dut_company_id(request, company_id: int) -> None:
        request.session[SessionService.SESSION_LAST_SET_DUT_COMPANY_ID] = company_id
        request.session.modified = True

    @staticmethod
    def get_last_set_dut_category_id(request) -> int:
        return request.session.get(SessionService.SESSION_LAST_SET_DUT_CATEGORY_ID, None)

    @staticmethod
    def set_last_set_dut_category_id(request, category_id: int) -> None:
        request.session[SessionService.SESSION_LAST_SET_DUT_CATEGORY_ID] = category_id
        request.session.modified = True

    @staticmethod
    def get_last_set_dut_location_id(request) -> int:
        return request.session.get(SessionService.SESSION_LAST_SET_DUT_LOCATION_ID, None)

    @staticmethod
    def set_last_set_dut_location_id(request, location_id: int) -> None:
        request.session[SessionService.SESSION_LAST_SET_DUT_LOCATION_ID] = location_id
        request.session.modified = True

    '''
    InspectionTemplate
    '''

    @staticmethod
    def get_last_set_template_company_id(request) -> int:
        return request.session.get(SessionService.SESSION_LAST_SET_TEMPLATE_COMPANY_ID, None)

    @staticmethod
    def set_last_set_template_company_id(request, company_id: int) -> None:
        request.session[SessionService.SESSION_LAST_SET_TEMPLATE_COMPANY_ID] = company_id
        request.session.modified = True

    @staticmethod
    def get_last_set_template_inspection_type_id(request) -> int:
        return request.session.get(SessionService.SESSION_LAST_SET_TEMPLATE_INSPECTION_TYPE_ID, None)

    @staticmethod
    def set_last_set_template_inspection_type_id(request, inspection_type_id: int) -> None:
        request.session[SessionService.SESSION_LAST_SET_TEMPLATE_INSPECTION_TYPE_ID] = inspection_type_id
        request.session.modified = True
