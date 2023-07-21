from wumpus import WumpusWorld

ENVIRONMENT_ROWS = 4
ENVIRONMENT_COLUMNS = 4
START_POINT = (3, 0)
PITS = [(0, 3), (1, 2), (3, 2)]
WUMPUS = (1, 0)
GOLD = (1, 1)
EPISODES = 500
EPSILON = 0.5
DISCOUNT_FACTOR = 0.9
LEARNING_RATE = 0.8

wumpus_agent = WumpusWorld(ENVIRONMENT_ROWS, ENVIRONMENT_COLUMNS, START_POINT, PITS, WUMPUS, GOLD,
                           EPISODES, EPSILON, DISCOUNT_FACTOR, LEARNING_RATE)

wumpus_agent.initialize()
print('Game Board')
print(wumpus_agent.rewards)
print('-------------------------------------------')
print('Start Training')
print('-------------------------------------------')
wumpus_agent.train()
print('Training Finished')
print("Path to hunt gold")
print(*wumpus_agent.best_path(START_POINT))
