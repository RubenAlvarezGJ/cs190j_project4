Style assumptions baked into this list: **4-directional sprites** (up / down / left / right), since LttP-era Zelda is 4-dir. Left can usually be a horizontal flip of right — generate **right only** unless the weapon/lighting makes it asymmetric. Most animated things become an `AnimatedSprite2D` (SpriteFrames) or an `AnimationPlayer` driving a sprite sheet. Tilesets go into `TileMap` / `TileSet` resources.

---

## 1. Player Character

The most-reused asset in the game. Plan the body once, then swap **gear skins** (see note below).

### Core animation set (per gear skin)
- [ ] Idle — 4 dir
- [ ] Walk / run — 4 dir
- [ ] Mine — 4 dir *(pickaxe skins only)*
- [ ] Attack — pickaxe — 4 dir
- [ ] Attack — katana — 4 dir
- [ ] Hurt / knockback — 4 dir (or 1 reusable)
- [ ] Death — 1
- [ ] Eat / heal — 1
- [ ] *(optional)* Push / pull (for boulders, doors) — 4 dir
- [ ] *(optional)* Pick-up / interact pose — 1

### Gear / skin variants (visual progression)
These each need their own sprite sheet because the silhouette changes:
- [ ] **Pre-shrine** — plain survivor, pickaxe (Tutorial → Factory → Watch Tower)
- [ ] **Backpack overlay** — visible pack added from Factory onward (can be a separate layered sprite drawn on top instead of a full reskin)
- [ ] **Post-shrine** — samurai armor + katana (Shrine onward, since both equip immediately there)
- [ ] *(optional)* upgraded-gear tint/variant after smithing (palette swap is enough)

> **Reuse tip:** layer the backpack and weapon as separate `Sprite2D` children anchored to the body, instead of re-drawing every frame. Cuts your player art roughly in half.

---

## 2. Enemies — Zombies

Difficulty escalates by count/speed/toughness, so design **one zombie rig** and create tiers mostly via **palette swaps + scale + stat tuning**. Generate distinct art only where you want a clear visual "uh-oh."

### Animation set (per tier that gets unique art)
- [ ] Walk / shamble — 4 dir
- [ ] Attack / lunge — 4 dir (or 1)
- [ ] Hurt — 1
- [ ] Death — 1
- [ ] *(optional)* Idle / spawn-rise — 1

### Tiers (map to your Flow Channel)
- [ ] **Shambler** — slow, tutorial *(unique art)*
- [ ] **Common** — Factory *(palette swap or light reskin)*
- [ ] **Feral / fast** — Forest *(unique art — speed should read visually)*
- [ ] **Brute / tough** — Village *(unique art — bigger silhouette)*
- [ ] **Climax / elite** — Water Dam *(unique art or armored variant)*

---

## 3. Environments / Tilesets (per area)

Each area is self-contained (no cross-area enemy persistence), so each can be its own `TileSet`. Note the **animated tiles** flagged below — Godot supports per-tile animation frames.

- [ ] **Tutorial** — ground, walls, mineable cave rock, simple boundary
- [ ] **Factory** — industrial floor/walls, machinery, pipes, conveyor *(animated)*, coal piles, bus stop
- [ ] **Military Watch Tower** — concrete, chain-link fence, the tower, sandbags, military crates
- [ ] **Shrine** — torii gate, stone path, lanterns *(animated flame)*, shrine building, weapon/armor pedestal
- [ ] **Forest** — grass, dirt path, trees, bushes, harvestable food plants
- [ ] **Village** — house exteriors, fences, well, market props, crafting-table spot
- [ ] **Water Dam** — dam concrete, **water tiles** *(animated)*, the boulder spot, sluice gates, control area

> Build a small **shared/global tileset** (cracks, rubble, generic shadows, edges) reused everywhere to keep areas cohesive and save work.

---

## 4. Props & Interactables (with states)

These drive your three core systems (Building, Smithing, Power) and the gates.

- [ ] **Mineable node** — coal/rock: full → cracked → broken (3 states + break particle)
- [ ] **Sewing machine** — idle + "crafting" animation (Building unlock)
- [ ] **Crafting / smithing table** — **unpowered** (coal-fed) and **powered** (electric) states + working anim (Smithing unlock)
- [ ] **Exit gate** — locked state, unlock animation, open state
- [ ] **Bus** — parked, doors open, drive-away (transition between areas)
- [ ] **TNT** — placed prop, lit fuse loop, (explosion VFX in §5)
- [ ] **Boulder** (Dam) — intact → cracked → destroyed
- [ ] **Dam mechanism / lever / valve** — off → on, restore animation
- [ ] *(optional)* breakable forest bush that drops food

---

## 5. Items, Pickups & Inventory Icons

Each generally needs a **world sprite** (lying in the level) and a matching **inventory/HUD icon**.

- [ ] Pickaxe
- [ ] Backpack — plus components: **leather, string, straps**
- [ ] Coal
- [ ] TNT (item form)
- [ ] Matches
- [ ] Katana
- [ ] Samurai armor
- [ ] Food / heals — 2–3 varieties (forest)
- [ ] Shields — base + upgraded tiers
- [ ] Crafting materials for smithing upgrades (if you add any)

---

## 6. VFX / Particles

Mostly Godot `GPUParticles2D` + a few sprite-sheet effects. The white "damage flash" is best done as a shader, not art.

- [ ] Mining hit sparks + rock debris
- [ ] Weapon swing arc — pickaxe
- [ ] Slash arc — katana
- [ ] Hit / blood splatter (zombie)
- [ ] Zombie death poof / dissolve
- [ ] **TNT explosion** (big — used to clear the Dam boulder)
- [ ] Heal / eat sparkle
- [ ] Pickup sparkle / shine
- [ ] **Gate unlock** glow
- [ ] **Power restored** surge (map-wide flourish when the Dam is fixed)
- [ ] Damage flash *(shader — note, not a sprite)*
- [ ] *(optional)* footstep dust, spawn dust for zombies

---

## 7. UI / HUD

- [ ] Health display — Zelda-style hearts (full / half / empty) or bar
- [ ] **Backpack / inventory** screen + slot grid
- [ ] Item icons (all of §5)
- [ ] **Wave / objective tracker** — "zombies X/Y" or round counter (core to every gate)
- [ ] **Crafting menu** (sewing machine — Building)
- [ ] **Smithing / upgrade menu** with price display (Smithing)
- [ ] Equip screen — weapon / armor / shield
- [ ] Interaction prompt ("Press E")
- [ ] Area-name title card / screen transition
- [ ] Tooltip / dialogue box (e.g., the "it'll be important later!" coal hint)
- [ ] Title screen, pause menu, game-over screen, victory screen

---

## 8. Audio

### SFX
- [ ] Footsteps (maybe per-surface: stone / grass / metal)
- [ ] Pickaxe swing + mine hit + node break
- [ ] Sword swing (katana)
- [ ] Hit flesh / zombie hurt
- [ ] Zombie idle groan + attack snarl + death
- [ ] Pickup / item get
- [ ] Craft success (sewing + smithing)
- [ ] Gate unlock
- [ ] TNT fuse + **explosion**
- [ ] Eat / heal
- [ ] Lever / switch / power-on hum
- [ ] Bus engine + horn
- [ ] Take damage + player death
- [ ] Menu navigate / select / back

### Music
- [ ] Title theme
- [ ] Tutorial (calm)
- [ ] Factory
- [ ] Forest / Shrine
- [ ] Village
- [ ] **Water Dam** (climax / high tension)
- [ ] Wave / combat tension layer (could be a stinger or layered track that kicks in during gates)
- [ ] Area-clear / victory sting

### Ambience (optional but cheap polish)
- [ ] Factory machinery hum, forest birds/wind, dam water rush, village wind

---

## Quick production-cost notes

- **Generate "right" only**, flip for left. Halves directional art for player + zombies.
- **Palette swaps** carry most of your zombie tiering and gear-upgrade visuals — far cheaper than new sprites.
- **Layer weapon/backpack** as child sprites on the player instead of redrawing full frames per gear state.
- **Shared tileset** of cracks/rubble/shadows reused across all 7 areas keeps the look consistent and the workload down.
- The heaviest unique-art buckets are: **player skins (×2 main)**, **zombie tiers (~4 unique)**, and **7 area tilesets**. Budget most of your time there.
