"""
Descripcion de las diferentes URLs utilizadas en el proyecto ZAPpm
"""

from django.conf.urls import patterns, url
from django.contrib import admin
from django.conf import settings
from django.contrib.auth.views import logout_then_login

from administrarLineaBase.views import generarCalculoImpacto, createLB, visualizarLB, workApplication, \
    crearSolicitudCambios, cancelarSolicitudCambios, visualizarSolicitud, votarSolicitud, revocarPermisos
from administrarReportes.views import reporte_proyecto, reporte_solicitud
from administrarTipoItem.views import createItemType, deleteItemType, itemTypeList, changeItemType, changeAtribute,\
    createAtribute, deleteAtribute, importItemType
from autenticacion.views import main, myLogin
from administrarUsuarios.views import createUser, changeUser, userList, userListJson, changePass, changeAnyUser
from zar.views import about, contact
from administrarProyectos.views import createProject, changeProject, projectList, workProject, setUserToProject, \
    changeProjectLeader, startProject, cancelProject, finProject, vistaDesarrollo, infoProject
from administrarFases.views import changePhase, createPhase, phaseList, deletePhase, importMultiplePhase,\
    confirmar_eliminacion_fase, workphase, finPhase, startPhase, subirOrden, bajarOrden, verFase
from administrarRolesPermisos.views import crearRol, eliminarRol, modificarRol, accesoDenegado
from administrarItems.views import createItem,\
    historialItemBase, relacionarItemBaseView, reversionItemBase, relacionarItemBase, \
    finalizarItem, validarItem, dardebajaItem, workItem, restaurarItem, verItem, finRevisionItem


admin.autodiscover()

urlpatterns = patterns('',
###################################################### AUTENTICACION ###################################################
                       url(r'^$', myLogin, {'template_name': 'autenticacion/login.html'}),
                       url(r'^login/$', myLogin, {'template_name': 'autenticacion/login.html'}),
                       url(r'^logout/$', logout_then_login, name="logout"),
                       url(r'^main/$', main, name="main"),
                       url(r'^about/$', about, name="about"),
                       url(r'^contact/$', contact),

###################################################### USUARIOS ########################################################
                       url(r'^createuser/$', createUser, name="createuser"),
                       url(r'^changeuser/$', changeUser, name="changeuser"),
                       url(r'^changeanyuser/(?P<id_usuario>\d+)$', changeAnyUser, name="changeanyuser"),
                       url(r'^userlist/$', userList, name="userlist"),
                       url(r'^userlistjson/(?P<tipoUsuario>[A-Z]{2})$', userListJson, name="userlistjson"),
                       url(r'^changepass/$', changePass, name="changepass"),
                       url(r'^forgot_password/$', 'django.contrib.auth.views.password_reset', {'template_name':'autenticacion/forgot_password.html',\
                               'post_reset_redirect' : 'registration/password_reset_done'}, name="reset_password"),
                       url(r'^forgot_password/registration/password_reset_done/$', 'django.contrib.auth.views.password_reset_done'),
                       url(r'^password_reset_confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
                           'django.contrib.auth.views.password_reset_confirm', {'post_reset_redirect': 'registration/password_reset_complete'}),
                       url(r'^/password_reset_complete/$', 'django.contrib.auth.views.password_reset_complete'),

###################################################### PROYECTOS #######################################################
                       url(r'^createproject/$', createProject),
                       url(r'^changeproject/(?P<id_proyecto>\d+)$', changeProject, name='changeproject'),
                       url(r'^changeprojectleader/(?P<id_proyecto>\d+)$', changeProjectLeader, name='changeprojectleader'),
                       url(r'^setusertoproject/(?P<id_proyecto>\d+)$', setUserToProject),
                       url(r'^projectlist/$', projectList, name='projectlist'),
                       url(r'^workproject/(?P<id_proyecto>\d+)$', workProject, name='workproject'),
                       url(r'^startproject/(?P<id_proyecto>\d+)$', startProject, name='startproject'),
                       url(r'^cancelproject/(?P<id_proyecto>\d+)$', cancelProject, name='cancelproject'),
                       url(r'^finproject/(?P<id_proyecto>\d+)$', finProject),
                       url(r'^infoproject/(?P<id_proyecto>\d+)$', infoProject),
                       url(r'^desarrollo/(?P<id_proyecto>\d+)$', vistaDesarrollo),


###################################################### FASES ###########################################################
                       url(r'^createphase/(?P<id_proyecto>\d+)$', createPhase),
                       url(r'^changephase/(?P<id_fase>\d+)$', changePhase),
                       url(r'^phaselist/(?P<id_proyecto>\d+)$', phaseList),
                       url(r'^importmultiplephase/(?P<id_fase>\d+)/(?P<id_proyecto_destino>\d+)$', importMultiplePhase),
                       url(r'^deletephase_confirm/(?P<id_fase>\d+)$', confirmar_eliminacion_fase),
                       url(r'^deletephase/(?P<id_fase>\d+)$', deletePhase),
                       url(r'^workphase/(?P<id_fase>\d+)$', workphase),
                       url(r'^finphase/(?P<id_fase>\d+)$', finPhase),
                       url(r'^startphase/(?P<id_fase>\d+)$', startPhase),
                       url(r'^subir/(?P<id_fase>\d+)$', subirOrden),
                       url(r'^bajar/(?P<id_fase>\d+)$', bajarOrden),

###################################################### ROLES ###########################################################
                       url(r'^createrole/(?P<id_proyecto>\d+)$', crearRol),
                       url(r'^changerole/(?P<id_proyecto>\d+)/(?P<id_rol>\d+)$', modificarRol),
                       url(r'^deleterole/(?P<id_proyecto>\d+)/(?P<id_rol>\d+)$', eliminarRol),
                       url(r'^denegado/(?P<id_error>\d+)$', accesoDenegado),
                       # TODO: Agregar paginas 404 y 500

###################################################### TIPO DE ITEMS ###################################################
                       url(r'^createitemtype/(?P<id_fase>\d+)$', createItemType),
                       url(r'^changeitemtype/(?P<id_tipoitem>\d+)$', changeItemType),
                       url(r'^itemtypelist/(?P<id_fase>\d+)$', itemTypeList),
                       url(r'^importitemtype/(?P<id_fase>\d+)/(?P<id_itemtype>\d+)$', importItemType),
                       url(r'^deleteitemtype/(?P<id_tipoitem>\d+)$', deleteItemType),
                       url(r'^infophase/(?P<id_fase>\d+)$', verFase),

###################################################### ATRIBUTOS #######################################################
                       url(r'^createatribute/(?P<id_tipoitem>\d+)$', createAtribute),
                       url(r'^changeatribute/(?P<id_atribute>\d+)$', changeAtribute),
                       url(r'^deleteatribute/(?P<id_atribute>\d+)$', deleteAtribute),

###################################################### ITEMS ###########################################################
                       url(r'^createitem/(?P<id_fase>\d+)$', createItem),
                       url(r'^workitem/(?P<id_item>\d+)$', workItem),
                       url(r'^historialitem/(?P<id_fase>\d+)/(?P<id_item>\d+)$', historialItemBase),
                       url(r'^relacionaritemvista/(?P<id_fase_actual>\d+)/(?P<id_item_actual>\d+)$', relacionarItemBaseView),
                       url(r'^revertiritem/(?P<id_item>\d+)/(?P<id_fase>\d+)/(?P<id_version>\d+)/$', reversionItemBase),
                       url(r'^relacionaritembase/(?P<id_item_hijo>\d+)/(?P<id_item_padre>\d+)/(?P<id_fase>\d+)/$', relacionarItemBase),
                       url(r'^generarcalculoimpacto/(?P<id_item>\d+)$', generarCalculoImpacto ),
                       url(r'^finalizaritem/(?P<id_item>\d+)$', finalizarItem ),
                       url(r'^validaritem/(?P<id_item>\d+)$', validarItem ),
                       url(r'^dardebajaitem/(?P<id_item>\d+)$', dardebajaItem ),
                       url(r'^restauraritem/(?P<id_item>\d+)$', restaurarItem ),
                       url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT, 'show_indexes': True} ),
                       url(r'^veritem/(?P<id_item>\d+)$', verItem ),
                       url(r'^veritem/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT, 'show_indexes': True} ),
                       url(r'^finrevisionitem/(?P<id_item>\d+)$', finRevisionItem ),


###################################################### LINEA BASE ######################################################
                       url(r'^createlb/(?P<id_fase>\d+)$', createLB ),
                       url(r'^visualizarlb/(?P<id_fase>\d+)$', visualizarLB ),

###################################################### SOLICITUD DE CAMBIOS ############################################
                       url(r'^crearsolicitud/(?P<id_fase>\d+)$', crearSolicitudCambios ),
                       url(r'^cancelarsolicitud/(?P<id_solicitud>\d+)/(?P<id_fase>\d+)$', cancelarSolicitudCambios ),
                       url(r'^workapplication/(?P<id_fase>\d+)$', workApplication ),
                       url(r'^visualizarsolicitud/(?P<id_solicitud>\d+)/(?P<id_fase>\d+)$', visualizarSolicitud ),
                       url(r'^createvote/(?P<id_solicitud>\d+)/(?P<voto>\d+)$', votarSolicitud),
                       url(r'^revocarPermisos/(?P<id_solicitud>\d+)$', revocarPermisos ),

###################################################### REPORTES ########################################################
                       url(r'^reporte_proyecto/(?P<id_proyecto>\d+)$', reporte_proyecto ),
                       url(r'^reporte_solicitud/(?P<id_proyecto>\d+)$', reporte_solicitud ),

                       )