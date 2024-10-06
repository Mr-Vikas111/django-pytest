from rest_framework import serializers

class BaseSerializer(serializers.ModelSerializer):
    
    def __init__(self, *args, **kwargs):

        """This init method is used for dynamic fields for serializer"""
        
        fields = kwargs.pop('fields', None)
        exclude = kwargs.pop('exclude', None)
        
        if fields is not None and exclude is not None:
            serializers.ValidationError("fields and serializers simultaneously not allowed")
        super().__init__(*args, **kwargs)
        
        if fields:
            for field in set(self.fields.keys()) - set(fields):
                self.fields.pop(field, None)
        if exclude:
            for field in set(exclude):
                self.fields.pop(field, None)

    
    
    def is_valid(self, bypass_validation=False, raise_exception=False):
        """This function is used to bypass_validation if needed in some case"""


        default_validation = super().is_valid(raise_exception)    
        return default_validation if not bypass_validation else True
    
    def to_internal_value(self, data):
        try:
            return super().to_internal_value(data)
        except serializers.ValidationError as exc:
            if type(data) == dict:
                custom_error_message = data.pop('error_message', None)
            else:
                custom_error_message = ""
            error_messages = {}
            for field, errors in exc.detail.items():
                field_errors = []

                for error in errors:
                    field_errors.append(str(error))
                error_messages[field] = field_errors
            error_messages['error_message'] = [custom_error_message] if custom_error_message else ['Something went wrong']
            raise serializers.ValidationError(error_messages)
    
    class Meta:
        abstract =True
