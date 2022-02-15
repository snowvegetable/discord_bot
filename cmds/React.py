from core.classes import *


class React(CogExtension):
    @commands.command()
    async def hi(self, ctx):
        await ctx.send("hi")


def setup(bot):
    bot.add_cog(React(bot))
