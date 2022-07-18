const { Client, Collection, Intents } = require('discord.js');

const client = new Client({partials: ["CHANNEL"], intents: [Intents.FLAGS.GUILDS, Intents.FLAGS.GUILD_MESSAGES, Intents.FLAGS.DIRECT_MESSAGES, Intents.FLAGS.GUILD_VOICE_STATES] });
const { getVoiceConnection,createAudioPlayer, AudioPlayerStatus,joinVoiceChannel,createAudioResource  } = require('@discordjs/voice');

client.on("messageCreate", (msg) => {
  if (msg.author.id == 406666674171936768 && msg.content == "LIT Rythm bot please play") {
    
    const voicechannel = msg.member.voice.channel
    const connection = joinVoiceChannel({
      channelId: voicechannel.id,
      guildId: msg.guild.id,
      adapterCreator: msg.guild.voiceAdapterCreator,
    })

    const player = createAudioPlayer();

    const resource = createAudioResource(__dirname + "/FinalChallenge.mp3");
    player.play(resource);
    const subscription = connection.subscribe(player);
    player.on(AudioPlayerStatus.Idle, () => {
      player.play(createAudioResource(__dirname + "/FinalChallenge.mp3"))
      // player.play(DiscordStream.createAudioResource(Ytstream(url, {filter : 'audioonly'})))
    })

  }else if(msg.author.id == 406666674171936768 && msg.content == "LIT Rythm bot please stop") {
    const connection = getVoiceConnection(msg.guild.id);
    console.log(connection);
    connection.destroy();
  }
});

client.login("OTk4NDY0ODg0MjEzODIxNTEx.G694Sb.o1zfMXLKhVbFjSUkUmVeBJb_dz7ZjEtosqqOA0");