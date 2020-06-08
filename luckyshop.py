import discord
import asyncio
import datetime

client = discord.Client()

token = "NzAzNTYzNDE1MjE3NzY2NDgw.XqQbKQ.exj4ov6D1MnU6KF-bbbGeZo8ops"

@client.event
async def on_ready():

    print("====================")
    print("다음으로 로그인 합니다 :")
    print(client.user.name)
    print("connection was successful")
    game = discord.Game("카톡 id - null9")
    print("====================")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.author.bot:
        return None
    if message.content == "!안녕":
        await message.channel.send("!안녕하세요!")
    if message.content.startswith("!대리"):    
        embed = discord.Embed(title="**대리 신청 방법**", description="1. __가격표__ 및 __대리전 유의상황__ 확인\n2. 준비 사항 확인 후 준비\n3. 신청 양식대로 작성 후 아래 티켓을 눌러 방에 입장 후 신청", color=0x37C7A9) 
        embed.set_thumbnail(url=message.guild.icon_url)
        embed.add_field(name="__**준비사항 - 스팀가드 해제(필수)**__", value="```Steam 설정 → STEAM GUARD 계정 보안 관리 → Steam Guard 해제 → 인증 메일 확인```", inline=False)
        embed.add_field(name="__**준비사항 - 클라우드 저장 활성화(필수)**__", value="```GTA5 실행 → Home 키 → 톱니바퀴 → 설정 → 게임 설정 → 클라우드 저장 활성화```", inline=False)
        embed.add_field(name="__**준비사항 - 나이트클럽 구매**__", value="```인터넷 → 메이즈 부동산 → 나이트 클럽 구매```\n※ 준비사항을 모두 준비하셔야 보다 작업을 빨리 끝낼 수 있으며, 스팀가드를 해제 안하시면 대리 순서가 뒤로 밀릴 수도 있습니다.", inline=False)
        embed.add_field(name="__**신청 양식**__", value="```세트 / 원하는 돈 / 원하는 레벨\n컬처랜드 문상 코드\n스팀 아이디 or 에픽게임즈 이메일 / 비밀 번호```\nex) 10000원 세트 / 8억 / 250\n1234 - 5678 - 9098 - 7654 or 765432\nhackmoney / hackmoney1234", inline=False)
        await message.channel.send(embed=embed)
client.run(token)