class Monkey(self):
    '''
    Base camp membership class
    '''
    def __init__(self, hash, fname, lname, c_score, leg_name, 
                 p_name, email, alpha_hash, phone, location, 
                 b_day, gender, sponsor, bio, avatar, pronoun, 
                 fb, insta, er_con, er_num):
        self.hash = hash #unique identifier
        self.fname = fname #first name
        self.lname = lname #last name
        self.c_score = c_score #current cap score
        self.leg_name = leg_name #legal name for policia
        self.p_name = p_name #nickname
        self.email = email #checked against profile
        self.alpha_hash = alpha_hash #concat name for url
        self.phone = phone #phone number
        self.location = location #location for ride share
        self.b_day = b_day #birthday
        self.gender = gender #avowed gender
        self.sponsor = sponsor #responsible party - should be hash
        self.bio = bio #copy intro
        self.avatar = avatar #official image to be used for wu
        self.pronoun = pronoun #not required  
        self.fb = fb #facebook id
        self.insta = insta #instagram id
        self.er_con = er_con #emergency name
        self.er_num = er_num #emergency number

    def fullname(self):
        return '{} {}'.format(self.fname, self.lname)


class Current(Monkey):
    '''
    Temporary camp membership class
    '''
    def __init__(self, optin, scat, scab, raw_work, work_unit, 
                 ticketed, accepted, virgin, intention, arrival, 
                 departure, arr_from, depart_to):
        super().__init__(hash, fname, lname, c_score, leg_name, 
                 p_name, email, alpha_hash, phone, location, 
                 b_day, gender, sponsor, bio, avatar, pronoun, 
                 fb, insta, er_con, er_num)
        self.optin = optin #required for engagement
        self.scat = scat #boolean
        self.scab = scab #boolean
        self.raw_work = raw_work #work count raw
        self.work_unit = work_unit #normalized work count
        self.ticketed = ticketed #ticketed/boolean
        self.accepted = accepted #permission given/boolean
        self.virgin = virgin #virgin/boolean
        self.intention = intention #intention for current cycle
        self.arrival = arrival #arrival on playa
        self.departure = departure #departure from playa
        self.arr_from = arr_from #location for launch
        self.depart_to = depart_to #location post-playa

class Tickets(Monkey):
    '''
    Distribution of information about passes class
    '''
    def __init__(self, bracket, tick, tick_type, wap, 
                 wap_origin, wap_date, tick_hash, tick_price, 
                 veh_pass, tick_que, dgs):
        self.bracket = bracket #slot identifier
        self.tick = tick #ticket identifier
        self.tick_type = tick_type #ticket origin
        self.wap = wap #work access pass
        self.wap_origin = wap_origin #work access pass origin
        self.wap_date = wap_date #date wap starts
        self.tick_hash = tick_hash #unique identifier for ticket
        self.tick_price = tick_price #price for ticket
        self.veh_pass = veh_pass #unique identifier for vehicle pass
        self.tick_que = tick_que #boolean/in or out of queue
        self.dgs = dgs #part of dgs

class Crew(Monkey):
    '''
    Class to organize groups of members
    '''
    def __init__(self,partners,p_type):
        self.partners = partners #hash of partner
        self.p_type = p_type #type of partnership

class History(Monkey):
    '''
    Maintain records of past performance 
    '''
    pass

class Fees(Monkey):
    '''
    Organization of fees associated with each member
    '''
    def __init__(self, c_fee, fee_tier, c_fee_date, meal_fee, 
                 work_deposit, water_fee, add_water, foam, bike_fee, 
                 bike_dep, lag_fee):
            pass

class Social(Monkey):
    '''
    Breakdown of social network within membership
    '''
    def __init__(self, circle, soc_lead, talent, talent_lead, 
                 teach, teach_lead, com_lead, placer, harpy, 
                 team_lead, team, rigger, rigger_lead):
            pass


class Placement(Monkey):
    '''
    Details of placement information class
    '''
    pass


