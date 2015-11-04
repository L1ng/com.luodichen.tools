'''
Created on Nov 4, 2015

@author: luodichen
'''
from django.template import Context, loader
from django.http.response import HttpResponse
import tabpage

class BaseResponse(object):
    def __init__(self, req):
        self.request = req
    
    def get_content(self):
        pass
    
    def get_active_index(self):
        pass
    
    def get_response(self):
        tab_list = tabpage.tablist
        tab_list[self.get_active_index()].active = True
        content = self.get_content()
        
        template = loader.get_template('mainframe.html')
        context = Context({
            'tab_list': tab_list,
            'tab_content': content,
        })
        
        return HttpResponse(template.render(context))

class IPResponse(BaseResponse):
    def __init__(self, req):
        BaseResponse.__init__(self, req)
    
    def get_content(self):
        template = loader.get_template('ip.html')
        context = Context({
        })
        
        return template.render(context)
    
    def get_active_index(self):
        return 0
