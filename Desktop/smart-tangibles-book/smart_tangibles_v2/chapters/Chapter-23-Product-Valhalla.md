# Chapter 23 - Product Valhalla

**When Service Evolves Into Relationship**

---

_Connected hardware products offer vendors the opportunity to provide continuous value to users through firmware updates and services, creating lasting relationships and increasing revenue. This shift in business model, exemplified by companies like Tesla and Apple, enables vendors to generate significant revenue from services and user engagement. Product management plays a crucial role in identifying and capitalizing on these opportunities for product innovation and user-centric development._

---



#### Product Management for the Physical World Series: Part VII

![](../images/maxresdefault.jpg)

https://youtu.be/iWI8bfK2wAQ?si=R-3I_4kdh8kpfDiH (link to video)

---



#### Service and relationship opportunities

Consider the scenario depicted in the video above. One morning in late November 2018, Elon Must tweeted the following:

![Elon Musk announces new Tesla features](../images/73dd11_8111524cfc4843618fd386a1d8218b12mv2.png)

Elon Musk announces new Tesla features

The next morning, some Tesla owners woke up to find "Romantic mode" as they tried to heat their cars in the chilly morning of November 30th.

![Automated FOTA message](../images/73dd11_97f7241586b44436b29245cdf4ee8955mv2.png)

Automated FOTA message

The update, automatically available after an overnight firmware update, also included gems such as "fart mode" which emulates flatulent sounds when the passengers take their seat. Class was never the hallmark of Mr Musk's endeavors, if one ever needed a reminder.

This FOTA functionality - Firmware Over The Air - allows technology vendors constantly improve their field deployed hardware, without recalling them to the lab or service station.

This approach bears many benefits at the operational level, reducing costly recalls, and ensuring broader standardization of the install base (think of the automatic updates of iOS, MacOS, Windows operating systems, constantly improving user functionality and security).

Funny and delighting as they might be, the Romantic / Fart modes offered by Tesla were far from the most radical, though.

In a series of other [<u><span>regular updates</span></u>](https://electrek.co/2019/11/01/tesla-model-3-long-range-increases-range-price/#:~:text=Tesla%20is%20as%20much%20a,to%20date%20and%20new%20cars.), users found their car's range (a coveted and anxiety inducing quantity for any electric vehicle owner), speed, and acceleration augmented overnight increasing.

Compare this to the slow progress offered by traditional car makers. You'd get a significant improvement in next year model, if at all.

---



#### The power of (commercial) relationships

Take a look at the following layer model for connected hardware products. You'll notice higher abstraction (and gradual distancing) from the physical hardware, and moving into the domain of services - not in the technical meaning of the word, but more in the sense of continuous value bestowed on the users, as long as the vendors want, that is:

![Proposed Layer model for connected products, and the value added services they offer](../images/73dd11_c0c67db1012b466682cdcfb97524e0cdmv2.png)

Proposed Layer model for connected products, and the value added services they offer

Indeed, these value added services (iTunes, Chrome browser and search, car navigation systems) create significant value to users, providing significant revenue opportunities, and reinforce customer loyalty: Users abhor the need to migrate their personal data between platforms, and value dearly the promise of a one-click hardware upgrade. We see that the technology of connected devices opens for improved (technical) service, but even more so, to increased opportunities for creating a lasting, meaningful, and positive customer relationship, that would pay in the next hardware replacement cycle.

---



#### Shifting the business model

Vendors place high value on the possibility to create and maintain a constant, meaningful, and positive relationship with their customers. Connected products offer this possibility for the first time, and industry pioneers are experimenting with it, creating a lot of additional value from it.

![Apple Inc. Revenue sources](../images/73dd11_b2d1ce74fdac4757abc34ab64ca59e6emv2.png)

Apple Inc. Revenue sources

Apple, originally a hardware vendor, manages to generate significant revenue from the Services segment, with a high gross margin of 71%, **mostly enabled by connected hardware.**

---



#### Conclusion

This series draws to an end, at least discussing the strategic trends driving hardware product innovation, and its impact on product management.  

Indeed, if Product Management embodies the discipline of identifying 'what to build', we are seeing new opportunities for early validation, de-risking, and building products users love.

> *Further, we can try and identify new opportunities for product evolution from a inert mass into a living and breathing ecosystem of physical and abstract capabilities, expanding user engagement and eventually increasing economic potential and value.*

---

### Chapter 9 - Validate, Before It's Too Late: De-risking physical products

_Physical product validation is crucial due to the high costs and inflexibility of hardware development. Market need and positioning analysis are essential, followed by feature validation through mockups, prototypes, and user testing. This process helps identify and prioritize features, ensuring the product meets user needs and aligns with market demands._



![Analytic dashboard showing events of interest](../images/nsplsh_4168344636672d4f6d6749mv2_d_4032_3024_s_4_2.jpg)

Analytic dashboard showing events of interest

---



#### Physical product validation MVP Challenge

An MVP, or a Minimally Viable Product, is a development stage used to create a new product with enough features to attract early adopter customers and validate an idea early in the development cycle.

While software products are easily amenable to this strategy, in part for their modularity and the vast underlying infrastructure in place.

Consider a mobile application, or a web app. Most of what's going on are infrastructures that cater to ALL apps, and are reused innumerable times.

![Software development - Standing on the shoulders of giants](../images/73dd11_93d837a0b2b14520bbc9dd38f8828387mv2.png)

Software development - Standing on the shoulders of giants

Note how shared web infrastructures, cloud included, are built to serve billions of users (beside your own app users).

It is fair to say app developers stand on the shoulders of giants, and as a result, the pace and scale of innovation they can bring is without match, notably because the infrastructure is built to support multiple tech-stacks and business cases, so that, should you pivot, you are not to loose a lot of the things that make your product tick.

---



**That is not the case with physical products.**

The challenge with meaningful MVP creation in hardware products is that, from a functional point of view, they are often <u><span>integrated monoliths</span></u>.

By this, I refer to the need to recreate almost every part of critical functional layers, with limited potential for component reuse.

Consider the main subsystems for a typical passenger car. These subsystems are characterized by different availability and development costs.

Notice that with the exemption of infotainment and control systems, the most differentiating factors are also the most expensive parts of any car development.

![Car Subsystems: Specificity, Cost, Value](../images/73dd11_288b543e7d204ee9b6a21fbea5e4e82bmv2.png)

Car Subsystems: Specificity, Cost, Value

The lead time and cost of recreation of manufacturing infrastructures and replenish critical inventories for these systems are much too prohibitive, and in fact are equivalent to the launch of a new model altogether.

Passenger cars are at the extreme of this continuum, but in general, physical product face similar rigidity in their development process, meaning that unless they operate within an extremely cash rich environment, physical product innovators have one bullet in their proverbial pistol.

This makes the challenge of early validation even more acute:

-   How can you experiment?

-   Can you bring your product in the hands of users, before all costs are sunk?

---



#### Problem Validation

> _"Fall in love with the problem, not the solution" (Uri Levine)_

This quotation addresses one of the most common fallacies within early stage product companies: Talented and motivated teams could and frequently would fall into the building stage fast. This is a symptom of a problem known as "a solution in search of a problem".

![A screaming robot. Sure you don't need one?](../images/73dd11_8d44e7d2a34d42ccbbc189b9d9626942mv2.jpg)

A screaming robot. Sure you don't need one? Source: *Green, K. (2013, January 9).* *On Fire* *[Comic strip]. Gunshow.* https://gunshowcomic.com/513

But whereas pivoting software products might still be possible (at cost), steering massive manufacturing infrastructures efforts oftentimes proves impossible. Usually there is not enough time, and not enough money to change course.

Validation, therefore, is key to success. But how does one do that?

---



#### Market need and Positioning

First comes a sound understanding of market dynamics (size, trends, and gaps), the competitive landscape, and customer needs.

From there, analyzing competitors’ features, language, and messaging allows us to build **positioning maps** – visualizing the “lines of battle” along which brands compete for space in customers’ minds. These dimensions form the axes for plotting different brands.

With established categories, this can be enriched with perception surveys: first asking a broad sample of customers which factors matter most to them (a qualitative research), then prioritizing these and having respondents rate brands along the selected attributes (a quantitative research). 

The aim is to capture perceptions – how customers *experience* and *rank* these qualities – rather than technical specifications, since positioning maps reflect the market’s mental landscape, not the manufacturer’s.

---



Consider as an example the following (hypothetical) perceptual map for the smartphone market, which is centered in this case around "feature - like" qualities: the available **range** of models, and the perceived **level of technology** integrated into the brand's product.

![Feature based perceptual map for smartphones](../images/73dd11_89b4b0146c914892a0ba4e4937514baamv2.png)

Feature based perceptual map for smartphones - [Interactive feature](https://yoelf22.github.io/positioning-map/perceptual_mapping_dashboard.html)

Were you a product manager for Pixel 7a in this example, you should be worried about the perception of your brand within the surveilled audience. There is a gap between the group of leaders and the rest - and your product is lagging.

If I were a product manager with Pixel 8Pro, I'd be thinking really hard how to build up performance and camera quality, to move further up the leaderboard.

Such perceptual maps help us understand our place (for existing brands), or where do we want to be, when planning new products. They show us what are the needs important to users and customers within the market segments we're after, therefore enabling us to design features tailored to better cater to them.



---



#### Feature scoping by competitive analysis

Consider the following competitive feature review by [<u><span>Insight Quantum</span></u>](https://www.linkedin.com/pulse/mastering-market-step-by-step-guide-crafting-comprehensive-wgfbc/), listing key features and their relative scores

| Car Model    | Horsepower (out of 5) | Torque (out of 5) | City MPG (out of 5) | Highway MPG (out of 5) | Crash Test Rating (out of 5) | Infotainment System (out of 5) | Driver Assist Features (out of 5) |
| ------------ | --------------------- | ----------------- | ------------------- | ---------------------- | ---------------------------- | ------------------------------ | --------------------------------- |
| Kia Seltos   | 4                     | 4                 | 4                   | 4                      | 5                            | 5                              | 4                                 |
| Competitor 1 | 3                     | 3                 | 3                   | 3                      | 4                            | 2                              | 2                                 |
| Competitor 2 | 5                     | 5                 | 5                   | 5                      | 5                            | 5                              | 4                                 |

Table 1: Competitive feature review (Insight Quantum)

The table can be translated into a spider graph:  

![Kia Seltos competitive analysis spider graph. Source: Insight Quantum](../images/73dd11_4b86e5789b7a4a758073fc4f3d68477emv2.png)

Kia Seltos competitive analysis spider graph. Source: Insight Quantum

When **building** a product, in contrast to **marketing** it, such competitive analysis is used to identify the areas where we want to shine, so that we can create our positioning statement and value proposition: In this example, a humorous one could be: "Crash safely with the music blasting on" – positioning Kia Seltos as the safest car with the best infotainment system.



---

#### Feature validation

The crucial part of the validation process are the insights we gained:

-   First we identify and prioritize the features according to our positioning

    -   These feature may be contradictory (such as performance vs. fuel efficiency)
-   We then stack the differentiating features on top of the conventional, foundational ones
-   Now we find a way to present these features to users, and have them experience them to the best of our ability.

    -   For instance, when we market automobiles, we can only inform consumers of our model's average fuel consumption, one tested in controlled environment to an industry agreed benchmark. This is only an indicative measure of economy, as no two drivers, trips, or load are the same, and the same goes for the actual fuel consumption consumers will experience eventually.

    -   In another context, when marketing future versions of complex products, we use **mockups** for the look and feel, well before starting production, and thus gage the audience's response prior to the large investments we are about to plough into the project.

CAF (Construcciones y Auxiliar de Ferrocarriles) is a spanish company which manufactures railway vehicles and equipment and buses.

Catering to the public transportation sector, their process includes bidding for open or close tenders, in which they present mockups showing their vision for the design and usability of the railroad car - ticking the boxes for the particular demands of the tender at hand.

![CAF mockup for a railroad car - NS sprinter](../images/73dd11_177c43641fa742b3a18b6efc10abcfe5mv2.jpg)

CAF mockup for a railroad car - NS sprinter

In this mockup for the [<u><span>NS sprinter</span></u>](https://www.facebook.com/reizigersov/posts/1079652722052431) series, for Dutch operator Nederlandse Spoorwegen, CAF shows the bodywork, as well as interiors, including electric sockets for passengers' devices, separate trash bins and toilets.

They have focus groups (including target users and customer representatives) experience this solution first hand, gage their responses, and draw necessary conclusions translated into design modifications

It is no small feat, either. Building a similar mockup can take nearly a year and cost up to a million euros. But once the green light is given, the manufacturer can confidently proceed with their multi-billion-euro project, which includes:

- Investments in manufacturing equipment

- Tooling

- Logistics (inventory provisioning for components and raw materials)

  ---

  

#### Limitations of user feedback

Of course, not every feature can be validated through mockups or public trials. To most users, the technicalities of drivetrains, energy consumption, or HVAC systems are little more than “tech babble.” Testing these in public would be nearly impossible, since most trial-and-error takes place in labs or on the factory floor, far from user experience.

Instead, these aspects are validated through proof-of-concepts carried out by the vendor under the oversight of the tender issuer, and are later bolstered through **technical specifications and performance guarantees** contractually committed, often as part of multi-decade operation agreements.

Together, these approaches highlight the dual nature of validation: user-facing features of look and feel are tested and refined through direct experience, while technical features are validated through experimentation, industry standards, and contractual commitments. Both dimensions are essential to building trust in complex products.

---



#### Validation as a Journey

Validation is never complete until users themselves perceive the value. Structured proxy methods – surveys, mockups, contractual guarantees – do provide a limited upfront confidence. Ultimately, the market decides in a moment: when a customer first touches, sees, or tries the product. The next chapters explore these decisive arenas of experiential validation, from the theater of public demos and unboxing to the disruptive force of killer features.