class Recommender(object):
    def __init__(self, sports):
        self.sports = sports
        
    def isRecommended(self, person, sport):
        if sport.minAge > person.age:
            return False
        if sport.onlyDisabled == True and person.isDisabled == False:
            return False
        if person.visionImpairment == True and sport.visionImpairment == False:
            return False
        return True
    def validateUserReqs(self, person):
        if not person.isDisabled:
            if person.visionImpairment or person.quad:
                return False
            return True
        else:
            if not (person.visionImpairment or person.quad):
                return False
            return True
            
    def getRecommendations(self, person):
        recs = []
        for sport in self.sports:
            if self.isRecommended(person, sport):
                recs.append(sport)
        return recs