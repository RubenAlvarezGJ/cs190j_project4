# fLoW — Game Context & Asset Reference

> **Purpose of this document.** This is a self-contained reference describing the game *fLoW* in full. It is written so that a language model with no prior knowledge of the project can (a) understand what the game is and how it plays, and (b) generate high-quality, consistent prompts for visual and audio asset generation. Read the whole document before writing any asset prompt; the **Visual Style** and **Asset Manifest** sections at the end depend on the context established earlier.

---

## 1. Elevator Pitch

*fLoW* is a 2D top-down action-adventure survival game set in a collapsed, post-apocalyptic world overrun by zombies. The player scavenges through the ruins of the old world — a dead factory, an abandoned military watch tower, an overgrown shrine, a ruined village, and a broken dam — fighting zombies and rebuilding the tools of civilization. The throughline is *restoration*: re-learning to carry and craft, recovering lost gear, and ultimately bringing the power back on. The player grows from a defenseless scavenger with a pickaxe into a katana-wielding, armored survivor.

## 2. Technical Profile

- **Engine:** Godot (2D).
- **Perspective / Art direction:** Top-down (overhead 3/4 view), 16-bit **SNES-era pixel art**, explicitly in the visual lineage of *The Legend of Zelda: A Link to the Past*.
- **Orientation & resolution:** Horizontal (landscape), **1920 × 1080**.
- **Required systems (per assignment):** Title scene with a Start button; a restart button on game-over; physics-based collision detection; animations for the player and every interactable component; sound effects for gameplay/physics interactions; background music; theme-appropriate fonts; at least three minutes of meaningful, actionable gameplay.
- **Course context:** This is a university game-design project (CMPSC 190J). Scope is deliberately bounded. It is *not* a full RPG.

## 3. Theme

**Post-apocalyptic adventure survival.** Civilization has collapsed and the world has gone dark. Nature is reclaiming human structures; rust, decay, and overgrowth are everywhere. The tone is gritty and tense but not gory or horror-shock — it must remain **rated "T for Teen."** Zombies are threatening but stylized, not graphically grotesque.

The emotional arc moves from *vulnerable and improvising* (early areas, scavenging for scraps to make a backpack) toward *capable and equipped* (later areas, armed and armored, restoring power to the world).

## 4. Core Mechanics

- **Mining** — using a pickaxe to break rocks/ore and gather materials (e.g., coal). Primary early-game verb. Has a swing animation; produces collision/impact feedback.
- **Attacking (combat)** — early on, improvised melee (pickaxe). After the Shrine, the player wields a **katana**. Combat is the central skill that escalates across the game.
- **Inventory / carrying (the Backpack)** — at the start the player *cannot carry materials*. A core early goal is assembling a backpack, which unlocks the ability to hold materials (for building), items, and heals.
- **Building** — first unlocked system. The player gathers backpack parts (leather, string, straps) and feeds them to a **sewing machine**, which produces the backpack. Establishes the "find parts → use a machine → produce a tool" loop.
- **Smithing** — second unlocked system. The player assembles a **crafting table** to upgrade weapons and shields for a cost. Requires power: initially powered by coal carried from the Factory, later by electricity once the dam is restored.
- **Power restoration** — third and final system. Restoring the **water dam** brings electricity back across the map (and powers smithing without coal). Gated behind using explosives (TNT from the Watch Tower) and matches found at the dam to clear a boulder.

### Progression spine (three unlock milestones)
1. **Unlock Building** + item carrying (backpack).
2. **Unlock Smithing** (weapon/shield upgrades).
3. **Restore Power** (electrify the map; final objective).

## 5. Enemies — Zombies (Hybrid Design)

- **Local + escalating:** Zombies belong to each area and get harder as the player advances (more numerous, faster, tougher in later areas). This is the backbone of the difficulty curve.
- **Wave / survival gates:** Each area is gated by a survival objective — clear a set number of zombies, or survive a set number of rounds — before the exit unlocks. Progression is *dependent on player success*.
- **Nested mini-curves:** Difficulty can ramp *within* an area across its waves, giving each location its own small flow curve inside the overall escalation.
- **No cross-area persistence:** Each area owns and frees its own zombies; leaving one area never drags enemies into the next. (Simpler to engineer; keeps the difficulty curve readable.)
- **Soft-lock safeguard:** During waves the player must always have a recovery path (backpack heals, forest food) so a gate can never trap an underpowered or out-of-healing player. Wave sizes should be tuned with this in mind.

## 6. Areas / Levels (in play order)

The game follows the **Flow Channel**: low skill / low difficulty → high skill / high difficulty. Gear and system unlocks are placed *just ahead of* difficulty spikes so the player is equipped to meet each rise.

| # | Area | Difficulty | What the player learns / does | Key unlocks | Zombie intensity |
|---|------|-----------|-------------------------------|-------------|------------------|
| 1 | **Tutorial** | Lowest | Pick up pickaxe & backpack; learn to mine; learn to attack | — | A few slow shamblers; small clear-gate |
| 2 | **Factory** | Low | Find coal (can't carry yet); find leather/string/straps; assemble backpack via sewing machine; carry coal out | **Building** + carrying | Slightly more; small wave gate |
| 3 | **Watch Tower / Shrine / Forest** | Medium | Find TNT (can't ignite yet); follow forest path to shrine; equip katana + samurai armor; forest holds food/heals | Katana + armor (gear spike *before* the wave) | Tougher/faster |
| 4 | **Village** | High | Assemble crafting table; upgrade weapons/shields (needs coal power) | **Smithing** | Hard waves requiring upgraded gear |
| 5 | **Water Dam** | Highest | Clear boulder with TNT + matches; restore dam; electrify the map | **Power restored** (final goal) | Hardest — climax wave |

**Transitions:** the player rides a **bus** between major areas ("hop on the bus / hop on daa buss").

## 7. Visual Style (read before writing any image prompt)

Consistency across assets is essential — every sprite must look like it belongs in the same game.

- **Medium:** 16-bit pixel art, SNES era. Hand-pixeled look, clean outlines, limited palette per sprite.
- **Perspective:** Top-down overhead with a slight 3/4 tilt (characters seen from above-front, like *A Link to the Past*). Tiles and props share this perspective — **no side-scroller / platformer framing**.
- **Palette:** Desaturated and muted overall — rust browns, ash grays, faded military greens, weathered concrete, dead-grass yellows, decay. Use a small number of **accent colors** to pop interactables: e.g., sickly green for zombies, warm orange for fire/coal/power, steel blue for restored electricity. Keep accents consistent in meaning.
- **Mood:** Gritty, overgrown, abandoned. Nature reclaiming machinery. Tense but not horror-gore; keep it T-for-Teen (stylized zombies, no graphic blood).
- **Sprite sizing (suggested, adjust to your tile grid):** base tile **16×16 px**; characters roughly **16×24** to **24×24 px**; render/scale up cleanly (nearest-neighbor, no smoothing) for the 1920×1080 target.
- **Animation:** every actor and interactable needs animation. Plan multi-frame sprite sheets (see manifest). Use 4-directional facing (up/down/left/right) for the player and zombies.

## 8. Asset Manifest

Grouped by the assignment's required categories. Each entry lists what to generate and the animation/variant notes a prompt should specify.

### 8.1 Player
- **Character sprite**, 4-directional (up/down/left/right).
- Animations: idle, walk/run, **mine** (pickaxe swing), **attack** (pickaxe early; **katana** after the Shrine), take-damage/hurt, death.
- **Equipment states:** unarmored scavenger → katana + **samurai armor** (a distinct armored look after the Shrine). Prompts should produce a matching armored variant of every animation, or an overlay.

### 8.2 Enemies (Zombies)
- **Base zombie**, 4-directional: idle, shamble/walk, attack/lunge, hurt, death (stylized, non-gory).
- **Difficulty variants** to read the escalation visually: e.g., slow shambler (early), faster/leaner runner (mid), bulkier/tougher brute (late). Keep them clearly the same "family" but distinguishable at a glance.

### 8.3 Environment & Tilesets (one cohesive set per area)
- **Tutorial:** simple ruined ground, scattered rock/ore to mine, a few obstacles.
- **Factory:** industrial interior/exterior — machinery, conveyor/pipes, coal seams, a **sewing machine** as a highlighted interactable.
- **Watch Tower / Forest / Shrine:** military concrete tower & crates (TNT prop); forest tileset (trees, undergrowth, food/forageables); an **overgrown shrine** with katana/armor pedestals.
- **Village:** ruined houses/streets; a **crafting table** interactable.
- **Water Dam:** the dam structure, water, a **boulder** to destroy, matches prop; visual "power off → power on" states (dark vs. lit/electrified).
- Each area needs: ground tiles, walls/collision props, decorative decay/overgrowth, and a clearly readable **exit/transition** (and a **bus** sprite for travel).

### 8.4 Items & Props (interactables — all need an animation or state change)
Pickaxe, backpack (+ its parts: leather, string, straps), coal, katana, samurai armor, food/heals, TNT, matches, sewing machine (operating animation), crafting table, boulder (intact → destroyed), power source / generator (off → on), bus.

### 8.5 UI
- **Title scene** background + logo/title treatment ("fLoW") in theme style.
- **Start** button; **game-over / restart** button.
- In-game HUD: health/heals indicator, inventory/backpack display, wave/objective counter (e.g., "zombies remaining" or "round X").

### 8.6 Sound Effects
Mining/pickaxe impact, melee/katana swing & hit, zombie sounds (groan, attack, death), player hurt, item pickup, crafting/sewing-machine & smithing operation, explosion (TNT), match strike, power-on hum/surge, UI clicks, area/wave-clear stinger.

### 8.7 Music
- **Title theme** — sets the post-apocalyptic mood.
- **Exploration loops** — ambient, tense, per-area variation welcome.
- **Wave/combat track** — more intense; can ramp with wave difficulty.
- **Victory / power-restored** cue for the finale.

### 8.8 Fonts
A worn, utilitarian, slightly industrial/decayed display font for the title/UI that fits a survival theme, plus a clean legible companion for body/HUD text. Must be readable at the target resolution.

## 9. How to Write Asset Prompts From This Document

When generating an individual asset prompt, always pin down:
1. **Style anchor** — "16-bit SNES pixel art, top-down 3/4 perspective, in the style of A Link to the Past."
2. **Subject + state** — exactly which sprite/animation frame(s) or tileset and which variant/state.
3. **Palette + mood** — pull from §7 (muted/decayed base, the correct accent color for the object's meaning).
4. **Format** — sprite sheet vs. single tile, directions, frame count, transparent background, target pixel dimensions, nearest-neighbor scaling.
5. **Consistency note** — that it must match the rest of the *fLoW* set described here.

> Keep every asset within the same palette and perspective so the five areas and all actors read as one cohesive world. When in doubt, favor restraint and decay over color and detail.
