# skill-scrum

This [opsdroid] skill allows project coordinators to trigger a round of scrums in a chat room.

# Requirements

None

# Configuration

```
- name: scrum
  repo: https://github.com/SolarDrew/skill-scrum.git
```

# Use

To trigger a scrum:

```
!scrum *some_user* *some_other_user* ...
```

Each of the mentioned users will be sent a direct message informing them that it's time for their scrum and how to respond.
To provide their answers, the users respond to the bot in either the private chat or main room with the tasks achieved yesterday, tasks scheduled for today and problems which might block progress:

```
!yesterday I made a cake
!today I will make a pie
!blockers I don't have any flour
```
