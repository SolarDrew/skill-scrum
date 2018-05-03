from opsdroid.matchers import match_regex

@match_regex("!scrum")
async def trigger_scrum(opsdroid, config, message):
    """Begin the scrum process for the specified users"""

    # Identify users to scrum
    users = message.text.split()[1:]

    # Overwrite any previous scrum info with blank structure for each user
    opsdroid.memory.put('scrum_info', {user: {} for user in users})

    # Create and join rooms with those users if not in one already, to listen for scrumming
    # Pending


async def report_scrum(opsdroid, config, message):
    """Get scrum input from users and report back into the main room when they've said all three things"""

    # Strip the command bit from the message

    # Add report to memory

    # If all three things have been reported, sent that info back to the main room
