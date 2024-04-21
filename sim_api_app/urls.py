from django.urls import path
from . import views

urlpatterns = [
    path("all-packs/", views.get_all_packs), #returns all packs to react
    path("all-traits/", views.get_all_traits), #returns all packs to react
    # path("single-pack/"), #might not need, get single pack
    path("lot-trait-filter/<int:pack_pk>", views.filter_lot_traits_by_pack), # returns the traits of the packs selected
    path("sim-trait-filter/<int:pack_pk>", views.filter_sim_traits_by_pack), # returns the traits of the packs selected
    path("ambition-filter/<int:pack_pk>", views.filter_ambition_by_pack), # returns the traits of the packs selected
    path("skills-filter/<int:pack_pk>", views.filter_sim_skills_by_pack), # returns the traits of the packs selected
]