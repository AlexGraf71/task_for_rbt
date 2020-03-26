class Search:
    def __init__(self, value=None, acceptance_conditions=None, there_is_a_mistake=None):
        self.value = value
        self.acceptance_conditions = acceptance_conditions
        self.there_is_a_mistake = there_is_a_mistake

    def __repr__(self):
        return "%s:%s:%s" % (self.value, self.acceptance_conditions, self.there_is_a_mistake)
