from behave import given, when, then
from shortcuts.ECs.ecs import (presenceID,
	                           presenceXP,
	                           visibilityXP,
	                           visibilityID)
from shortcuts.finds.singular import (findID,
	                                  findXP)
from shortcuts.finds.plural import (findIDs,
	                                  findXPs)
from shortcuts.ACs.acs import hover
from features.features.T_Shirts_Tab.T_Shirts_Tab_page_object import elements as e


@when("I click on the T_SHIRTS button")
def i_click_tshirts_button(context):
    presenceXP(context, e["TSHIRTS_button"])
    findXP(context, e["TSHIRTS_button"]).click()

@when("I click on the FADED T_SHIRT button")
def i_click_faded_tshirt_button(context):
    presenceXP(context, e["faded_tshirt"])
    findXP(context, e["faded_tshirt"]).click()

