from django import forms

UPLOAD_EXTENSIONS = ["pdf"]


class PdfForm(forms.Form):

    year = forms.IntegerField(label="Enter Year",
                                  required=True)

    variable  = year = forms.IntegerField(label="Enter Year",
                                  required=True)

    document = forms.FileField(label="Balance Sseet",
                                  required=True)

    def clean_document(self):
        """
        Enforce file type
        :return:
        """
        curr_file = self.cleaned_data['document']
        if not enforce_file_extension(curr_file.name, UPLOAD_EXTENSIONS):
            raise forms.ValidationError('Invalid file format. '
                                        'Can only upload file types {}'.\
                                format(' '.join(UPLOAD_EXTENSIONS)))

    
def enforce_file_extension(file_name, allowed_file_types):
    if not file_name:
        return False

    file_name = file_name.split('.')

    extension = file_name[-1]

    if extension in allowed_file_types:
        return True

    return False