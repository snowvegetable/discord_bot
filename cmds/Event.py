from core.classes import *


class Event(CogExtension):
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(int(jdata["channel"][0]))
        await channel.send(f'{member} join!')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.bot.get_channel(int(jdata["channel"][0]))
        await channel.send(f'{member} leave!')

    @commands.Cog.listener()
    async def on_message(self, msg):
        keyword = ['apple', 'pen', 'pie', 'abc']
        if msg.content in keyword and msg.author != self.bot.user:
            await msg.channel.send('apple')


def setup(bot):
    bot.add_cog(Event(bot))
