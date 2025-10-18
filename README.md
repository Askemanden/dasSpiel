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

https://trello.com/b/TVuGyqtP
