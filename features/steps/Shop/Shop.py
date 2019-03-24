from behave import given, when, then
from shortcuts.ECs.ecs import (presenceID,
	                           presenceXP,
	                           visibilityXP,
	                           visibilityID)
from shortcuts.finds.singular import (findID,
	                                  findXP)
from shortcuts.finds.plural import (findIDs,
	                                  findXPs)
from features.features.Shop.Shop_page_object import elements as e


@when("I click on the SHOP button")
def i_click_dresses_button(context):
    presenceXP(context, e["SHOP_button"])
    findXP(context, e["SHOP_button"]).click()
