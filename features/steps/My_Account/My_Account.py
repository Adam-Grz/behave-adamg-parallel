from behave import given, when, then
from shortcuts.ECs.ecs import (presenceID,
	                           presenceXP,
	                           visibilityXP,
	                           visibilityID)
from shortcuts.finds.singular import (findID,
	                                  findXP)
from shortcuts.finds.plural import (findIDs,
	                                  findXPs)
from features.features.My_Account.My_Account_page_object import elements as e


@when("I click on the MY_ACCOUNT button")
def i_click_dresses_button(context):
    presenceXP(context, e["MY_ACCOUNT_button"])
    findXP(context, e["MY_ACCOUNT_button"]).click()
