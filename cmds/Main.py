from core.classes import *


class Main(CogExtension):
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"{round(self.bot.latency * 1000)}")


def setup(bot):
    bot.add_cog(Main(bot))
