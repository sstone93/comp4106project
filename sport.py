class Sport(object):
    def __init__(self, id, type, name, minAge, city, onlyDisabled, visionImpairment, quad, expReq):
        self.id = id
        self.type = type
        self.name = name
        self.minAge = minAge
        self.city = city
        self.onlyDisabled = onlyDisabled
        self.visionImpairment = visionImpairment
        self.quad = quad
        self.expReq = expReq
        
    def toString(self):
        result = ""
        result = result + self.type + " through " + self.name + " in " + self.city
        
        if self.onlyDisabled == True:
            result = result + " open to participants with "
            if self.visionImpairment:
                result = result + " a visual impairment "
            if self.quad:
                result = result + " quadriplegia "
        else:
            result = result + " open to participants of all abilities "
            
        if self.minAge == 0:
            result = result + "no minimum age requirement "
        else:
            result = result + "must be at least " + str(self.minAge) + " years old "
            
        if self.expReq:
            result = result + "prior experience needed."
            
        else:
            result = result + "no previous experience required."
        
        return result