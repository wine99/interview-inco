# Remote Controlling API

## Purpose
When interviewing a candidate, we believe that an interview based on a pre-solved assignment opens up the conversation and will be more interesting for both parties.

It is important to emphasize that the assignment doesn't have a right or wrong answer - instead it acts as a basis for a discussion and enables us to get an idea of how you approach a task. <b>We do not require that you implement all listed requirements as long as you can describe how you would approach the missing pieces, and the submitted code demonstrates your coding skills. 

Feel free to challenge any requirements.</b>

> In the gas department of InCommodities, we mostly use Python, and please use primarily this language. 

## Description

You control a park of 5 wind turbines. For the sake of simplicity we'll assume that they always produce at max capacity.
| Turbine  | Capacity (MWh) | Production cost (€/MWh) |
|---|---|---|
| A  | 2  | 15  |
| B  | 2  | 5  |
| C  | 6  | 5  |
| D  | 6  | 5  |
| E  | 5  | 3  |

Each turbine above is described with three values. One being the turbine identifier, the second being how much power (MW) the turbine can produce per hour, and lastly the cost of running the turbine.

<b>Requirements</b>

- Keep the turbine online only if you earn money on it, i.e. if the market price exceeds the production cost.
- Run as many turbines as needed to reach the specified production target. Production target must not be exceeded.
- When choosing which turbines to run, prioritize the cheapest production first while still respecting the other requirements.
- Change in production target are submitted as a delta increase/decrease.
- Production target must be greater than or equal to 0 and not exceed the total maximum capacity for the park.

> In order to respect the requirements the current production may be less than the production target.

<b>Goal</b>

With those requirements in mind, your goal is to implement a system that manages such a park. You need to create:

- One background service acting as a restful HTTP server enabling the calling user to:
    - Submit an increase in the park's production target.
    - Submit a decrease in the park's production target.
    - Submit the current market price (price limit).
    - Retrieve a list of the turbines combined with their respective expected production (0 if not running, otherwise max. capacity).

- One front-end service containing all the business logic and managing the park. This service must communicate with the HTTP-serving service in order for that one to fulfil its requirements towards the user.

> Note, that this is a toy example for you to demonstrate your skills within coding, system architecture and user interaction - not market knowledge or wind production optimization skills.

<b>Example</b>

<b>1.</b>
Set limit price to <b>6€</b>.
Increase production target by <b>10MWh</b>. 
The production plan now looks as follows:
| Turbine  | Expected production |
|---|---|
| A  | 0  | 
| B  | 2  | 
| C  | 0  | 
| D  | 0  | 
| E  | 5  | 
<i>Sum production: <b>7MWh</b></i>
<i>Target production: <b>10MWh</b>; Price limit: <b>6€</b></i>

<b>2.</b>
Increase production target by <b>5MWh</b>. Now sums to <b>15MWh</b>.
The production plan now looks as follows:
| Turbine  | Expected production |
|---|---|
| A  | 0  | 
| B  | 2  | 
| C  | 6  | 
| D  | 0  | 
| E  | 5  | 
<i>Sum production: <b>13MWh</b></i>
<i>Target production: <b>15MWh</b>; Price limit: <b>6€</b></i>

<b>3.</b>
Set limit price to <b>4€</b>.
The production plan now looks as follows:
| Turbine  | Expected production |
|---|---|
| A  | 0  | 
| B  | 0  | 
| C  | 0  | 
| D  | 0  | 
| E  | 5  | 
<i>Sum production: <b>5MWh</b></i>
<i>Target production: <b>15MWh</b>; Price limit: <b>4€</b></i>