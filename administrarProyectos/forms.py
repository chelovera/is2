#encoding=utf-8
from django.forms import ModelForm
from django import forms
import floppyforms as forms2

from administrarProyectos.models import Proyecto, UsuariosVinculadosProyectos
from autenticacion.models import Usuario


class NewProjectForm(ModelForm):
    """
    *Formulario para la creación de nuevos proyectos en el sistema. Utilizamos el modelo de* ``Proyecto``
    *definido del cual filtramos los campos de tal manera a que solo se habiliten los
    campos necesarios para la creación de un proyecto en el sistema.*

    Opción válida solo para usuarios con rol de ``Administrador``.

    :param args: Argumentos para el modelo base ``ModelForm``.
    :param kwargs: Keyword Arguments para la función ``ModelForm``.

    ::

        class Meta:
            model = Proyecto
            fields = ('nombre', 'lider_proyecto', 'descripcion',)

    """
    lider_proyecto = str(forms.ModelChoiceField(widget=forms.CheckboxSelectMultiple, queryset=Usuario.objects.all(),
                                                label='Líder de Proyecto', required=True, ))


    class Meta:
        model = Proyecto
        fields = ('nombre', 'lider_proyecto', 'descripcion',)


    def __init__(self, *args, **kwargs):
        super(NewProjectForm, self).__init__(*args, **kwargs)


class ChangeProjectForm(forms.ModelForm):
    """
    *Formulario para la modificación de proyectos creados en el sistema.  Utilizamos el modelo de* ``Proyecto``
    *definido del cual filtramos los campos de tal manera a que solo se habiliten los
    campos disponibles para la modificación de un proyecto en el sistema.*

    Opción válida solo para usuarios con rol de ``Administrador``.

    :param args: Argumentos para el modelo base ``ModelForm``.
    :param kwargs: Keyword Arguments para la función ``ModelForm``.

    ::

        class Meta:
            model = Proyecto
            fields = ('nombre', 'lider_proyecto', 'descripcion',)

    """

    class Meta:
        model = Proyecto
        fields = ('nombre', 'lider_proyecto', 'descripcion',)

    def __init__(self, *args, **kwargs):
        super(ChangeProjectForm, self).__init__(*args, **kwargs)
        f = self.fields.get('user_permissions', None)
        if f is not None:
            f.queryset = f.queryset.select_related('content_type')


class ChangeProjectLeaderForm(forms2.ModelForm):
    """
    *Formulario para la modificación de proyectos creados en el sistema.  Utilizamos el modelo de* ``Proyecto``
    *definido del cual filtramos los campos de tal manera a que solo se habiliten los
    campos disponibles para la modificación de un proyecto en el sistema.*

    Opción válida solo para usuarios con rol de ``Lider``.

    :param args: Argumentos para el modelo base ``ModelForm``.
    :param kwargs: Keyword Arguments para la función ``ModelForm``.

    ::

        class Meta:
            model = Proyecto
            fields = ('nombre', 'lider_proyecto', 'descripcion',)

    """

    class Meta:
        model = Proyecto
        fields = ('nombre', 'fecha_inicio', 'fecha_fin', 'descripcion', 'observaciones')
        widgets = {
            'nombre': forms2.TextInput(attrs={'class': 'form-control', }),
            'fecha_inicio': forms2.DateInput(attrs={'class': 'form-control', }),
            'fecha_fin': forms2.DateInput(attrs={'class': 'form-control', }),
            'descripcion': forms2.Textarea(attrs={'class': 'form-control', }),
            'observaciones': forms2.Textarea(attrs={'class': 'form-control', }),
        }

    def __init__(self, *args, **kwargs):
        super(ChangeProjectLeaderForm, self).__init__(*args, **kwargs)
        f = self.fields.get('user_permissions', None)
        if f is not None:
            f.queryset = f.queryset.select_related('content_type')

class setUserToProjectForm(forms2.ModelForm):
    """
    *Formulario para vincular usuarios a un proyecto*

    :param args: Argumentos para el modelo base ``ModelForm``.
    :param kwargs: Keyword Arguments para el modelo ``ModelForm``.
    """
    cod_usuario = str(forms.ModelChoiceField(widget=forms.Select, queryset=Usuario.objects.all(),
                                         label='Usuarios Disponibles', required=True, ))

    class Meta:
        model = UsuariosVinculadosProyectos
        fields = ('cod_usuario',)


    def __init__(self, *args, **kwargs):
        super(setUserToProjectForm, self).__init__(*args, **kwargs)
