from django import forms


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    _from = forms.EmailField(label="Votre adresse email")
    copy = forms.BooleanField(help_text="Cochez si vous souhaitez obtenir une copie du mail envoyé", required=False)

    # # validation message
    # def clean_message(self):
    #     message = self.cleaned_data['message']
    #     if "pizza" in message:
    #         # ici message d'erreur en haut du form
    #         raise forms.ValidationError("On ne veut pas entendre parler de pizza !")
    #
    #     return message

    # validation titre & message
    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        sujet = cleaned_data.get('subject')
        message = cleaned_data.get('message')

        if sujet and message:
            if "pizza" in sujet and "pizza" in message:
                # ici message d'erreur au niveau des inputs
                self.add_error("message",
                               "Vous parlez déjà de pizzas dans le sujet, "
                               "n'en parlez plus dans le message !"
                               )

        return cleaned_data
