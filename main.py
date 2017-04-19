from sport import *
from Recommender import *
from Person import *

def main():
    sports = []
    sport = Sport(1, "Basketball", "Ottawa Carleton Wheelchair Sports Association", 0, "Ottawa", False, False, False, False)
    sports.append(sport)
    sport = Sport(2, "Rugby", "Ottawa Stingers", 15, "Ottawa", True, False, True, False)
    sports.append(sport)
    sport = Sport(3, "Track and Field", "Ottawa Lions", 0, "Ottawa", True, True, True, False)
    sports.append(sport)
    sport = Sport(4, "Sledge Hockey", "Sledge Hockey of Eastern Ontario", 6, "Eastern Ontario", True, False, True, False)
    sports.append(sport)
    sport = Sport(5, "Tennis", "National Capital Wheelchair Tennis Association", 0, "Ottawa", True, False, True, False)
    sports.append(sport)
    sport = Sport(6, "Table Tennis", "National Capital Wheelchair Tennis Association", 0, "Ottawa", True, False, True, False)
    sports.append(sport)
    sport = Sport(7, "Skiing", "Ski Hawks", 3, "Ottawa", True, True, False, False)
    sports.append(sport)
    sport = Sport(8, "Rugby", "Toronto Titans", 15, "Toronto", True, False, True, False)
    sports.append(sport)
    sport = Sport(9, "Swimming", "Brock Niagara Penguins", 15, "Niagara", True, True, True, True)
    sports.append(sport)
    sport = Sport(10, "Boccia", "Ottawa Boccia Club", 15, "Ottawa", True, False, True, False)
    sports.append(sport)
        
    recommender = Recommender(sports)

    print recommender
    
    print "Welcome to the para sport recommendation system"
    print "-----------------------------------------------"
    print ""
    print "To receive recommendation, enter your personal information as instructed."
    print "Type 'Quit' at any time to exit the program."
    
    done = False
    
    while done == False:
        resp = raw_input("What is your age? ")
        if (resp == "Quit"):
            done = True
            break
            
        while (not resp.isdigit()) or (int(resp) < 0 or int(resp) > 100):
            resp = raw_input("What is your age? ")
            if (resp == "Quit"):
                done = True
                break
                
        age = int(resp)
        
        
        answer = False
        while answer == False:
            resp = raw_input("Do you have a disability? (y/n) ")
            if resp == "y":
                isDisabled = True
                answer = True
            elif resp == "n":
                isDisabled = False
                answer = True
                
        if isDisabled:
            answer = False
            while answer == False:
                resp = raw_input("Do you have a visual impairment? (y/n) ")
                if resp == "y":
                    visualImpairment = True
                    answer = True
                elif resp == "n":
                    visualImpairment = False
                    answer = True
                    
            answer = False
            while answer == False:
                resp = raw_input("Are you a quadriplegic? (y/n) ")
                if resp == "y":
                    quad = True
                    answer = True
                elif resp == "n":
                    quad = False
                    answer = True
        
        else:
            visualImpairment = False
            quad = False
        
        person = Person(age, isDisabled, visualImpairment, quad)
        
        if not recommender.validateUserReqs(person):
            print "Invalid specifications, try again."
            
        else:
            recs = recommender.getRecommendations(person)
            print "RECOMMENDATIONS"
            print "---------------"
            for rec in recs:
                print rec.toString()
                print "------------------------------------------------------------------------------"
    
if __name__ == "__main__":
    main()