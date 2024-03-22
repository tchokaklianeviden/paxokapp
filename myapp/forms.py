from django import forms

from .models import Col

class ColForm(forms.ModelForm):
    class Meta:
        model = Col
        fields = ["col_name", "col_code", "col_alt", "col_lat", "col_lon", "col_type" ]	

    def is_valid(self):        
        col_name = self.data["col_name"]                
        col_code = self.data["col_code"]                
        col_alt = self.data["col_alt"]            
        col_lat = self.data["col_lat"]        
        col_lon = self.data["col_lon"]        
        col_type = self.data["col_type"]        
    
        if Col.objects.filter(col_code=col_code).exists():            
            ####
            #
            #cols = Col.objects.filter(col_code=col_code)
            #for myCol in cols:
            #    myCol.col_name = col_name                            
            #    myCol.col_code = self.data["col_code"]                            
            #    myCol.col_alt = col_alt           
            #    myCol.col_lat = col_lat       
            #    myCol.col_lon = col_lon      
            #    myCol.col_type = col_type
            #    myCol.save()            
            return False    
        return True