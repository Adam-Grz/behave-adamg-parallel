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
from features.features.Women_Tab.Women_Tab_page_object import elements as e


@when("I click on the WOMEN button")
def i_click_women_button(context):
    presenceXP(context, e["WOMEN_button"])
    findXP(context, e["WOMEN_button"]).click()

@when("I hover over the WOMEN button")
def i_click_women_button(context):
    presenceXP(context, e["WOMEN_button"])
    women_button = findXP(context, e["WOMEN_button"])
    hover(context, women_button)
    visibilityXP(context, e["TOPS_hover"])

@when("I click on the TOPS header")
def i_click_women_button(context):
    presenceXP(context, e["TOPS_hover"])
    findXP(context, e["TOPS_hover"]).click()

