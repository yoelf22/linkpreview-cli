# The Commitment Space: Visualizing Hardware vs Software Decisions

## Overview

The Commitment Space is a two-dimensional framework for understanding where product decisions fall based on their reversibility characteristics. It helps product managers apply appropriate rigor to different types of decisions — and identify opportunities to architecturally shift decisions from high-commitment to low-commitment zones.

![The Commitment Space](commitment_space_chart.png)

---

## The Two Dimensions

### X-Axis: Cost to Reverse

From negligible (left) to catastrophic (right). This includes:
- **Direct costs**: Tooling, materials, engineering labor, third-party services
- **Time costs**: Schedule delays, lead times, coordination overhead
- **Opportunity costs**: What else could have been built with those resources

**Scale anchors:**
| Position | Cost Range | Examples |
|----------|------------|----------|
| <$1K | Negligible | Config changes, copy updates, A/B tests |
| ~$10K | Low | App refactoring, API versioning, firmware parameters |
| ~$50K | Moderate | PCB respin, firmware architecture changes |
| ~$100K | High | Injection mold modifications, new certifications |
| >$250K | Very High | Major tooling changes, full redesigns, product recalls |

### Y-Axis: Risk if Wrong

From minor inconvenience (bottom) to existential threat (top). This considers:
- **User impact**: Safety, functionality, experience degradation
- **Business impact**: Revenue loss, support costs, churn
- **Regulatory impact**: Compliance violations, mandatory recalls
- **Reputation impact**: Brand damage, trust erosion

**Scale anchors:**
| Position | Severity | Examples |
|----------|----------|----------|
| Trivial | No user-visible impact | Analytics event naming |
| Minor | User inconvenience, easily corrected | App UI awkwardness |
| Significant | User frustration, support burden | Feature doesn't work as expected |
| Major | Product failure, financial loss | Core functionality broken |
| Existential | Safety recall, regulatory action | Battery fire, security breach |

---

## The Four Quadrants

### Q1: Danger Zone (Upper Right)
**High cost, high risk — Validate exhaustively**

Hardware decisions cluster here. These are one-way doors that define your product for its entire lifecycle. Mistakes are expensive to fix and dangerous if wrong.

**Decisions in Q1:**
- Battery chemistry and thermal design
- Safety certifications (UL, CE, FCC)
- Core processor/SoC selection
- Injection mold tooling
- Product form factor
- Wireless protocol selection
- PCB layout and component placement

**Required approach:**
- Full Stage-Gate process
- Extensive prototyping and user testing
- FMEA and risk analysis
- Multiple design reviews
- Supplier qualification

### Q2: High Stakes (Upper Left)
**Low cost, high risk — Validate heavily**

Firmware decisions live here. They're cheaper to change than hardware (via FOTA), but failures can brick devices or create security vulnerabilities.

**Decisions in Q2:**
- FOTA update mechanism design
- Bootloader architecture
- Firmware security model
- Core RTOS selection
- Communication protocol implementation

**Required approach:**
- Staged rollouts (1% → 10% → 100%)
- Automatic rollback mechanisms
- Extensive testing before deployment
- Canary deployments
- Monitoring and alerting

### Q3: Safe Zone (Lower Left)
**Low cost, low risk — Experiment freely**

Software decisions cluster here. This is where traditional software PM frameworks excel. Move fast, learn fast, iterate weekly.

**Decisions in Q3:**
- Mobile app UI/UX
- Cloud API design
- Push notification content
- Onboarding flows
- Dashboard layouts
- Feature flags and experiments
- Pricing and packaging
- Marketing copy

**Required approach:**
- Lean Startup / Build-Measure-Learn
- A/B testing
- RICE prioritization
- Continuous deployment
- Data-driven iteration

### Q4: Waste Zone (Lower Right)
**High cost, low risk — Avoid or simplify**

Decisions here represent over-engineering — spending significant resources on things that don't differentiate or matter to users.

**Decisions in Q4:**
- Over-engineered packaging
- Custom connectors when standard would work
- Premium materials for non-visible components
- Unnecessary certifications
- Gold-plated features nobody requested

**Required approach:**
- Question the decision itself
- Simplify or eliminate
- Use standard/commodity solutions
- Redirect resources to Q1 or Q3

---

## Strategic Movement: Q1 → Q3

The strategic opportunity in smart tangibles is **architecturally shifting decisions from Q1 toward Q3**.

Every capability you can move from hardware to software:
- Reduces cost of iteration
- Decreases risk of being wrong
- Increases speed of learning
- Preserves optionality longer

**Examples of Q1 → Q3 shifts:**

| Instead of... (Q1) | Consider... (Q3) |
|-------------------|------------------|
| Physical buttons for each function | Touchscreen UI or app control |
| Fixed LED indicator meanings | Firmware-configurable LED patterns |
| Hardcoded sensor thresholds | Cloud-configurable thresholds |
| Fixed display layouts | Firmware-updatable UI screens |
| Hardware security tokens | Software/cloud authentication |
| Printed user manual | In-app guidance, updateable |

---

## The Firmware Bridge

Firmware uniquely spans Q2 and Q3, depending on what you're changing:

| Firmware Decision | Quadrant | Rationale |
|-------------------|----------|-----------|
| Bootloader design | Q2 | Safety-critical, rarely changed |
| FOTA mechanism | Q2 | Must work perfectly from day one |
| Core architecture | Q2 | Pervasive impact, hard to refactor |
| Feature additions | Q2-Q3 | FOTA updatable, but testing burden |
| Algorithm tuning | Q3 | Parameter changes, lower risk |
| Config flags | Q3 | Instant change, minimal risk |

**The firmware test:** Before any firmware change, ask:
1. What's the blast radius if this goes wrong?
2. Can we roll back automatically?
3. What percentage of fleet should see this first?

---

## Using the Commitment Space

### In Planning Sessions

Plot your upcoming decisions on this space:
- Are you applying Stage-Gate rigor to something in Q3?
- Are you moving fast on something in Q1?
- Mismatches signal process problems

### In Architecture Discussions

For each planned capability, ask:
- "Can we move this point left?" (reduce cost)
- "Can we move this point down?" (reduce risk)
- "Can we move it to a different layer entirely?"

### In Prioritization

- Q1 decisions should be made early and validated thoroughly
- Q3 decisions can be deferred and experimented with freely
- Q4 decisions should be questioned or eliminated

### Decision Authority by Quadrant

| Quadrant | Validation Required | Decision Authority |
|----------|--------------------|--------------------|
| Q1 | Maximum — Stage-Gate, prototypes, FMEA | Executive/founder |
| Q2 | High — staged rollouts, testing, rollback plans | Product + Engineering leads |
| Q3 | Minimal — hypothesis + metrics | Product manager |
| Q4 | Question the decision itself | Anyone can flag |

---

## Methodology Note

Decision positions in the Commitment Space visualization are estimated based on the author's experience across consumer electronics, industrial IoT, and smart home products. The X-axis represents approximate cost to reverse a decision (combining direct costs, engineering time, and delay impact). The Y-axis represents risk severity if the decision proves wrong (from minor inconvenience to existential/recall-level threat).

**Cost anchors based on industry benchmarks:**

| Decision Type | Typical Cost Range | Source |
|---------------|-------------------|--------|
| Injection mold tooling | $50K–$500K | Industry surveys, manufacturing quotes |
| PCB prototype + respin | $10K–$50K | PCB manufacturer pricing |
| FCC certification | $15K–$50K | FCC fee schedules + testing lab quotes |
| Major product recall | $5M–$5B+ | Allianz Product Recall Reports; Samsung Note 7 ($5.3B) |
| Mobile app deployment | ~$0 marginal | Industry standard |
| FOTA update deployment | <$0.01/device | AWS IoT / Azure IoT pricing |

Positions are illustrative — actual costs and risks vary significantly by product complexity, production volume, company scale, and industry. The model's value lies in relative positioning and quadrant membership, not precise coordinates.

---

## Key Takeaways

1. **Not all decisions are equal.** Hardware decisions are fundamentally different from software decisions in their commitment characteristics.

2. **Smart tangibles span all quadrants.** Unlike pure hardware or pure software, connected products require managing decisions across the entire space.

3. **Architecture determines flexibility.** The boundaries between quadrants are set by architectural decisions made early. You can't retrofit reversibility.

4. **Push decisions toward Q3 whenever possible.** Every capability moved from hardware to software increases your ability to iterate and learn.

5. **Match rigor to quadrant.** Applying Stage-Gate to Q3 decisions slows you down. Applying Lean Startup to Q1 decisions gets you killed.

---

*This explainer accompanies the article "Product Management Frameworks for Smart Tangibles" and draws from concepts in the forthcoming book on product management for smart, connected, software-augmented hardware.*
