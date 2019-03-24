from behave import given
from shortcuts.ECs.ecs import (presenceID,
	                           presenceXP,
	                           visibilityXP,
	                           visibilityID)
from shortcuts.finds.singular import (findID,
	                                  findXP)
from shortcuts.finds.plural import (findIDs,
	                                  findXPs)


@given("I have navigated to the main page")
def navigated_to_main_page(context):
    context.driver.get("http://practice.automationtesting.in")
