from opsdroid.matchers import match_regex

@match_regex("!scrum")
async def trigger_scrum(opsdroid, config, message):
    """Begin the scrum process for the specified users"""

    # Identify users to scrum
    users = message.text.split()[1:]

    # Overwrite any previous scrum info with blank structure for each user
    await opsdroid.memory.put('scrum_info', {user: {} for user in users})

    # Create and join rooms with those users if not in one already, to listen for scrumming
    # Pending


@match_regex("!yesterday")
@match_regex("!today")
@match_regex("!blockers")
async def report_scrum(opsdroid, config, message):
    """Get scrum input from users and report back into the main room when they've said all three things"""

    scrum_info = await opsdroid.memory.get('scrum_info')
    if message.user not in scrum_info.keys():
        return

    for command in ["!yesterday", "!today", "!blockers"]:
        if command in message.text:
            # Strip the command bit from the message
            report = message.text.replace(command, '')
            # Add report to memory
            scrum_info[message.user][command] = report
            await opsdroid.memory.put('scrum_info', scrum_info)

    # If all three things have been reported, sent that info back to the main room
    reports = scrum_info[message.user]
    reported = reports.keys()
    if "!yesterday" in reported and "!today" in reported and "!blockers" in reported:
        await message.respond(f"""{message.user}'s scrum report:
        - *Yesterday:* {reports["!yesterday"]}
        - *Today:* {reports["!today"]}
        - *Blockers:* {reports["!blockers"]}
        """)
