# dasSpiel

**Wir machen das Spiel des Übermenschen**

## Koncept

Et 2-dimensionelt overlevelsesspil, hvor burgeren kan udforske verdenen omkring sig, og verden genererer omkring spilleren. Verdenen genereres ud fra et seed, som er et tal. Dette tillader generatoren at generere to identiske verdener, skulle det samme seed angives til spillet.

## Inspirationsmateriale

Hollow knight (Den har intet at gøre med spillet, men den fortjener det)
2d minecraft
Top down Terraria
Don’t starve together
Don’t starve together
Legend of Zelda – A link between worlds

## Roller

| Aske | Louis | Jacob |
| ---- | ----- | ----- |
| S.M. |       |       |

## How to run
For at køre programmet kan exe filen main.exe fra dist folderen køres.
Alternativt kan programmet køres med python interpreteren enten ved at køre main.py fra ens IDE eller med `python main.py` i kommandolinjen. For denne metode sørg for at have alle biblioteker installeret. Disse findes i requirements.txt og kan installeres med kommandoen `pip install -r requirements.txt`

## FLOWCHARTS OG KLASSEDIAGRAMMER

```mermaid
classDiagram
    %% ==== PLAYER ====
    class Player {
        - Vector2i grid_position
        - Vector2f world_position
        - int health
        - float speed
        - tuple color
        - Vector2f final_world_position
        - list~Vector2f~ subtargets
        - Inventory inventory
        - list~Vector2i~ path

        + __init__(health:int, speed:float=0.15, grid_position:Vector2i, color:tuple)
        + draw(screen:pygame.Surface) void
        + set_path(path:list~Vector2i~, final_world_position:Vector2f) void
        + _shared_point(a:Vector2i, b:Vector2i) Vector2f|None
        + newTarget(params:list[[int,int], World]) bool
        + update(dt:float) void
        + interact(params:list[[int,int], World]) bool
    }

    %% ==== WORLD ====
    class World {
        - int seed
        - list changes
        - PerlinNoise biomeNoise
        - Vector2i current_chunk_pos
        - Chunk chunk
        - Biome current_biome
        - list~Feature~ features
        - dict~Vector2i,Tile~ real_tiles

        + __init__() 
        + generate_chunk() Chunk
        + draw(surface:pygame.Surface) void
    }

    class Chunk {
        - Biome biome
        - list~Feature~ features
        - dict~Vector2i,Tile~ tiles

        + __init__(biome:Biome, features:list~Feature~, tiles:dict~Vector2i,Tile~)
        + __str__() str
    }

    %% ==== TILE ====
    class Tile {
        - Vector2i position
        - bool passable
        - pygame.Surface texture
        - Signal on_interact
        - MINING_TYPE mining_type
        - Item loot

        + __init__(x:int, y:int, passable:bool, mining_type:MINING_TYPE, texture:pygame.Surface, loot:Item|None)
        + __str__() str
        + draw(surface:pygame.Surface) void
        + interacted(interacter:Item, inventory:Inventory) void
    }

    class Stone {
        + __init__(x:int, y:int, biome:BiomeTypes)
    }
    class Wood {
        + __init__(x:int, y:int, biome:BiomeTypes)
    }
    class Bush {
        + __init__(x:int, y:int, biome:BiomeTypes)
    }

    Stone --|> Tile
    Wood --|> Tile
    Bush --|> Tile

    %% ==== INVENTORY ====
    class Inventory {
        - list~Item~ items
        - Item equipped
        - bool opened

        + __init__()
        + addItem(item:Item) void
    }

    class Item {
        - bool equipable
        - list~MINING_TYPE~ miningTypes

        + __init__(equipable:bool, miningTypes:list~MINING_TYPE~)
    }

    class Hand {
        + __init__()
    }
    class StoneBlock {
        + __init__()
    }
    class WoodBlock {
        + __init__()
    }
    class Apple {
        + __init__()
    }

    Hand --|> Item
    StoneBlock --|> Item
    WoodBlock --|> Item
    Apple --|> Item

    class MINING_TYPE {
        <<enumeration>>
        NONE
        STONE
        WOOD
        BUSH
    }

    %% ==== FEATURE ====
    class FeatureTypes {
        <<enumeration>>
        ROCK
        BUSHES
        LENGTH
    }

    class Feature {
        - int world_seed
        - Vector2i chunk_pos
        - int type
        - Vector2i position
        - BiomeTypes biome
        - list~Tile~ tiles

        + __init__(position:Vector2i, type:float, biome:BiomeTypes, chunk_pos:Vector2i, world_seed:int)
        + make_tiles() list~Tile~
        + __str__() str
    }

    %% ==== BIOME ====
    class BiomeTypes {
        <<enumeration>>
        FOREST
        MOUNTAIN
        LENGTH
    }

    class Biome {
        - BiomeTypes type
        - pygame.Surface texture

        + __init__(type:float)
        + __str__() str
        + draw(surface:pygame.Surface) void
    }

    %% ==== SIGNAL ====
    class Signal {
        - list~[str, Callable[[list], bool]]~ connections

        + __init__()
        + connect(name:str, func:Callable[[list], bool]) void
        + remove(name:str) void
        + emit(params:list) void
    }

    %% ==== VECTORS ====
    class Vector2 {
        - float x
        - float y

        + __init__(x, y)
        + change_values(x, y) void
        + length() float
        + distance_to(other:Vector2) float
        + normalize() Vector2f
        + direction_to(other:Vector2) Vector2f
        + __add__(other:Vector2) Vector2
        + __sub__(other:Vector2) Vector2
        + __truediv__(scalar:float) Vector2
        + __mul__(scalar:float) Vector2
        + __iadd__(other:Vector2) Vector2
        + __itruediv__(scalar:float) Vector2
        + __isub__(other:Vector2) Vector2
        + __imul__(scalar:float) Vector2
        + __str__() str
        + __repr__() str
        + __eq__(other:Vector2) bool
        + __hash__() int
    }

    class Vector2f {
        + __init__(x:float, y:float)
    }

    class Vector2i {
        + __init__(x:int, y:int)
        + change_values(x:int, y:int) void
    }

    Vector2f --|> Vector2
    Vector2i --|> Vector2

    %% ==== RELATIONSHIPS ====
    Player --> Inventory : has
    Player --> World : uses
    Player --> Tile : interacts
    World --> Chunk : contains
    Chunk --> Biome : has
    Chunk --> Feature : has
    Chunk --> Tile : has
    Chunk --> Vector2i : ´has
    Tile --> Inventory : interacts
    Tile --> Item : drops
    Tile --> MINING_TYPE : requires
    Inventory --> Item : contains
    Feature --> FeatureTypes : uses
    Feature --> Tile : creates
    Feature --> BiomeTypes : uses
    Biome --> BiomeTypes : has
    Tile --> Signal : uses
    Tile --> Vector2i : has
    Player --> Vector2i : has
    Player --> Vector2f : has
    World --> Vector2i : chunk_pos
    Feature --> Vector2i : has

```

### Main

```mermaid
flowchart TD
    A["main()"] --> B["pygame.init()
    screen = pygame.display.set_mode(...)
    pygame.display.set_caption(...)
    world = World()
    player = Player(health=10)
    leftClick = Signal()
    rightClick = Signal()"]

    B --> C["leftClick.connect('move player', player.newTarget)
    
    rightClick.connect('interact', player.interact)"]

    C --> D["running = True
    clock = pygame.time.Clock()
    dt = 0"]

    D --> E["for event in pygame.event.get()"]
    E --> F{"event.type == QUIT"}
    F -- Yes --> G["running = False"]
    F -- No --> H["continue"]

    G --> I["player.update(dt)
    screen.fill((0,0,0))
    world.draw(screen)
    player.draw(screen)
    pygame.display.flip()
    dt = clock.tick(1)"]
    H --> I

    I --> J{"while running"}
    J -- True --> J1{if main_menu == True}
    J1 -- True --> J2[world.draw(screen)
    player.draw(screen)
    paused_text.draw(screen)
    esc_menu(quit_menu, screen)
    continue]
    J2 --> J1
    J1 -- False --> K["for event in pygame.event.get()"]
    K --> L{"event.type == QUIT"}
    L -- Yes --> M["running = False"]
    L -- No --> N{"event.type == MOUSEBUTTONDOWN"}
    N -- Yes --> O{"event.button == LEFT or RIGHT"}

    O -- LEFT --> P["leftClick.emit([event.pos, world])
    print('l')"]
    O -- RIGHT --> Q["print('r')
    rightClick.emit([event.pos, world])"]
    O -- No --> K

    P --> R["player.update(dt)
    screen.fill((0,0,0))
    world.draw(screen)
    player.draw(screen)
    pygame.display.flip()
    dt = clock.tick(60)"]
    Q --> R
    N -- No --> R
    R --> J

    %% End
    J -- False --> S["pygame.quit()"]
    S --> T["end main()"]

```

### Pathfind flowcharts
#### astar
```mermaid
flowchart TD
    A["astar(start, goal, blocked)"] --> B{"goal in blocked"}
    B -- Yes --> Z["return None"]
    B -- No --> C{"goal == start"}
    C -- Yes --> Z["return None"]
    C -- No --> D["directions = 8-neighbors
    open_set = []
    counter = 0
    heappush(open_set, (0.0, counter, start))
    counter += 1
    came_from = {}
    g_score = { start: 0.0 }"]

    D --> E{"open_set not empty"}
    E -- No --> Z["return None"]
    E -- Yes --> F["_, _, current = heappop(open_set)"]
    F --> G{"current == goal"}
    G -- Yes --> H["path = []
    while current in came_from:
        path.append(current)
        current = came_from[current]
    path.append(start)
    return reversed(path)"]
    G -- No --> I["for (dx, dy) in directions"]
    I --> J{"can_move(current, dx, dy, blocked)"}
    J -- No --> I
    J -- Yes --> K["nx = current.x + dx
    ny = current.y + dy
    neighbor = Vector2i(nx, ny)
    tentative_g = g_score[current] + move_cost(dx, dy)"]
    K --> L{"neighbor not in g_score OR tentative_g < g_score[neighbor]"}
    L -- Yes --> M["g_score[neighbor] = tentative_g
    f_score = tentative_g + heuristic(neighbor, goal)
    heappush(open_set, (f_score, counter, neighbor))
    counter += 1
    came_from[neighbor] = current"]
    L -- No --> I
    M --> I
    I --> E

```

#### can_move
```mermaid
flowchart TD
    A["can_move(current, dx, dy, blocked)"] --> B{"dx != 0 AND dy != 0"}
    B -- Yes --> C["side_a = (current.x + dx, current.y)
    side_b = (current.x, current.y + dy)
    blocked_a = is_blocked(side_a.x, side_a.y, blocked)
    blocked_b = is_blocked(side_b.x, side_b.y, blocked)"]
    C --> D{"blocked_a OR blocked_b"}
    D -- Yes --> Z["return False"]
    D -- No --> E["nx = current.x + dx
    ny = current.y + dy
    return in_bounds(nx, ny) AND Vector2i(nx, ny) not in blocked"]
    B -- No --> E
```

#### is_blocked
```mermaid
flowchart TD
    A["is_blocked(x, y, blocked)"] --> B["in = in_bounds(x, y)"]
    B --> C{"NOT in OR Vector2i(x, y) in blocked"}
    C -- Yes --> Z["return True"]
    C -- No --> Z["return False"]
```

#### in_bounds
```mermaid
flowchart TD
    A["in_bounds(x, y)"] --> B{"0 <= x < MAP_WIDTH AND 0 <= y < MAP_HEIGHT"}
    B -- Yes --> Z["return True"]
    B -- No --> Z["return False"]
```

#### move_cost
```mermaid
flowchart TD
    A["move_cost(dx, dy)"] --> B{"dx != 0 AND dy != 0"}
    B -- Yes --> Z["return sqrt(2)"]
    B -- No --> Z["return 1.0"]
```
#### heuristic
```mermaid
flowchart TD
    A["heuristic(a, b)"] --> B["dx = abs(a.x - b.x)
    dy = abs(a.y - b.y)
    m = min(dx, dy)
    return (dx + dy) + (sqrt(2) - 2) * m"]
```

### Player flowcharts

#### set_path
```mermaid
flowchart TD
    A["set_path(path, final_world_position)"] --> B{"path == None"}
    B -- Yes --> Z["return"]
    B -- No --> C["path.pop(0)"]
    C --> D["self.path = path"]
    D --> E["self.final_world_position = final_world_position"]
    E --> F["self.subtargets.clear()"]
    F --> G{"path empty?"}
    G -- Yes --> Z["return"]
    G -- No --> H["for cell in path"]
    H --> I["cell_center = Vector2f(...)"]
    I --> J["corner = _shared_point(prev_cell, cell)"]
    J --> K{"corner != None"}
    K -- Yes --> L["subtargets.append(corner)"]
    K -- No --> M["skip"]
    L --> M
    M --> N["subtargets.append(cell_center)"]
    N --> O["prev_cell = cell"]
    O --> H
    H --> P["subtargets.pop()"]
    P --> Q["subtargets.append(final_world_position)"]
    Q --> Z["end"]

```

#### _shared_point
```mermaid
flowchart TD
    A["_shared_point(a, b)"] --> B["dx = b.x - a.x, dy = b.y - a.y"]
    B --> C{"abs(dx) > 1 OR abs(dy) > 1"}
    C -- Yes --> Z["return None"]
    C -- No --> D["ax = a.x*TILE_SIZE + TILE_SIZE/2"]
    D --> E["ay = a.y*TILE_SIZE + TILE_SIZE/2"]
    E --> F["return Vector2f(ax + dx*TILE_SIZE/2, ay + dy*TILE_SIZE/2)"]
```

#### newTarget
```mermaid
flowchart TD
    A["newTarget(params)"] --> B["worldTarget = Vector2f(params[0])"]
    B --> C["target = Vector2i(worldTarget // TILE_SIZE)"]
    C --> D["world = params[1]"]
    D --> E["blocked = []"]
    E --> F["for tile in world.real_tiles.values()"]
    F --> G{"tile.passable == False"}
    G -- Yes --> H["blocked.append(tile.position)"]
    G -- No --> F
    H --> F
    F --> I["path = astar(self.grid_position, target, blocked)"]
    I --> J["set_path(path, worldTarget)"]
    J --> Z["return False"]
```

#### update
```mermaid
flowchart TD
    A["update(dt)"] --> B{"subtargets empty?"}
    B -- Yes --> Z["return"]
    B -- No --> C["target = subtargets[0]"]
    C --> D["move_vec = target - world_position"]
    D --> E{"move_vec.length() > 0"}
    E -- Yes --> F["direction = move_vec.normalize()"]
    F --> G["world_position += direction * speed * dt"]
    E -- No --> H["skip"]
    G --> I{"(target - world_position).length() < speed*dt"}
    H --> I
    I -- Yes --> J["world_position = target"]
    J --> K["subtargets.pop(0)"]
    K --> L{"path not empty AND world_position == path[0] center"}
    L -- Yes --> M["grid_position = path.pop(0)"]
    L -- No --> N["skip"]
    M --> O["print(grid_position)"]
    N --> O
    I -- No --> O
    O --> Z["end"]
```

#### interact
```mermaid
flowchart TD
    A["interact(params)"] --> B["interact_position = Vector2i(params[0])"]
    B --> C["world = params[1]"]
    C --> D["grid_interact_position = interact_position // TILE_SIZE"]
    D --> E["tile = world.real_tiles.get(grid_interact_position)"]
    E --> F{"tile == None"}
    F -- Yes --> Z["return False"]
    F -- No --> G{"tile.position.distance_to(grid_position) >= 3"}
    G -- Yes --> Z["return False"]
    G -- No --> H["tile.interacted(inventory.equipped, inventory)"]
    H --> I["print(inventory.items)"]
    I --> Z["return True"]
```

### World Flowcharts

#### generate_chunk
```mermaid
flowchart TD
    A["generate_chunk"] --> B["Compute seed from world_seed * chunk_pos.length()"]
    B --> C["Create feature_noise with seed"]
    C --> D["biome = Biome(noise(...))"]
    D --> E["features = []"]
    E --> F["Loop over grid with FEATURE_FREQUENCY"]
    F --> G["noise_val = feature_noise(...)"]
    G --> H["features.append(Feature(...))"]
    H --> F
    F --> I["tiles_list = []"]
    I --> J["For each feature: extend tiles_list with feature.tiles"]
    J --> K["tiles = {}"]
    K --> L["For each tile in tiles_list: tiles[tile.position] = tile"]
    L --> M["return Chunk(biome, features, tiles)"]
```

### Signal Flowcharts
#### emit
```mermaid
flowchart TD
    A["emit(params)"] --> B["Loop over connections"]
    B --> C["consumed = func(params)"]
    C --> D{"consumed == True?"}
    D -- Yes --> Z["Break loop"]
    D -- No --> B
    B --> Z["End"]
```


https://trello.com/b/TVuGyqtP
