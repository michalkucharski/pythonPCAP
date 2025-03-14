
import random
#the script which pick the random number from the proposed series of numbers from 0 to max_number
def generate_tickets(ticket_count, max_number):

    pickedNum = random.sample(range(0, max_number), ticket_count)
    return (pickedNum, random.sample(pickedNum, 1)[0])