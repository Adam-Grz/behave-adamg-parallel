from behave import given, when, then
from shortcuts.ECs.ecs import (presenceID,
	                           presenceXP,
	                           visibilityXP,
	                           visibilityID)
from shortcuts.finds.singular import (findID,
	                                  findXP)
from shortcuts.finds.plural import (findIDs,
	                                  findXPs)
from features.features.Dresses_Tab.Dresses_Tab_page_object import elements as e


@when("I click on the DRESSES button")
def i_click_women_button(context):
    presenceXP(context, e["DRESSES_button"])
    findXP(context, e["DRESSES_button"]).click()

@when("I click on the CASUAL_DRESSES button")
def i_click_women_button(context):
    presenceXP(context, e["CASUAL_DRESSES_button"])
    findXP(context, e["CASUAL_DRESSES_button"]).click()

@when("I click on the EVENING_DRESSES button")
def i_click_women_button(context):
    presenceXP(context, e["EVENING_DRESSES_button"])
    findXP(context, e["EVENING_DRESSES_button"]).click()
