# Problem- Game Play Analysis I
# Leetcode and Difficulty Level- 511 and Easy
select distinct player_id,min(event_date) as first_login
from activity
group by player_id

