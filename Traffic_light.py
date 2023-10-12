import random as rand

# Weights to every state of traffic light
weight_global = [0, 0, 0]

# Traffic light states, 0 - no light, 1 - light; 0 - RED; 1 - YELLOW; 2 - GREEN.
inp_global = [[1, 0, 0],
              [0, 1, 0],
              [0, 0, 1]]

# Decisions for every state of traffic light
goal_decision_global = [0, 0, 1]

# Function that changes weight for one case
def change_weight(weight, inp, goal_prediction):
    error = 0
    decision = 0
    smooth = 0.01

    for i in range(len(inp)):
        decision = inp[i] * weight
        error = decision - goal_prediction
        weight -= (error * inp[i]) * smooth

    print("Weight " + str(weight))
    print("Prediction  " + str(decision))

    return weight

# Function that changes weight for all cases
def adjust_weights(n):
    for i in range(n):
        print("\n")
        print("Iteration " + str(i))
        for j in range(0, 3):
            weight_global[j] = change_weight(weight_global[j], inp_global[j], goal_decision_global[j])


# Function that makes decision with already correct weights
def make_prediction(weight, inp):
    decision = 0
    for i in range(len(inp)):
        decision += inp[i] * weight[i]
    if decision > 0.998:
        print("GO!")
    else:
        print("Stand still")

# Firstly, it make weights correct
adjust_weights(9990)

# It chooses state of traffic light
traffic_light_state = rand.randint(0, 2)

# Block that convert digital values to linguistic meanings
traffic_light_state_description = ""
if traffic_light_state == 0:
    traffic_light_state_description = "RED"
elif traffic_light_state == 1:
    traffic_light_state_description = "YELLOW"
else:
    traffic_light_state_description = "GREEN"

# It shows the final decision
print(
    "Traffic light state: " + str(inp_global[traffic_light_state]) + ", that mean: " + traffic_light_state_description)
make_prediction(weight_global, inp_global[traffic_light_state])
