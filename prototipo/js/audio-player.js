/**
 * TUNA DE LA FACULTAD DE DERECHO DE ALMERÍA
 * Reproductor Musical del Cancionero (audio-player.js)
 */

const TunaAudioPlayer = {
  tracks: [
    {
      title: 'Noche de Ronda en Almería',
      album: 'Álbum Oficial XXV Aniversario',
      duration: '3:45',
      durationSec: 225,
      notes: [440, 494, 523, 587, 659, 587, 523, 494],
      lyrics: `Noche de ronda, qué triste pasas,\nqué triste cruzas por mi balcón.\nNoche de ronda, cómo me hieres,\ncómo lastimas mi corazón...\n\nPor la Alcazaba baja la tuna,\ncantan sus voces bajo la luna,\ny entre las rejas de la Judería,\ndeja un suspiro por Almería.`
    },
    {
      title: 'Clavelitos Tradicionales',
      album: 'Clásicos de la Universidad',
      duration: '2:50',
      durationSec: 170,
      notes: [523, 587, 659, 698, 784, 698, 659, 587],
      lyrics: `Mocita dame el clavel,\ndame el clavel de tu boca,\nque para eso no hay que tener\nmucha vergüenza ni poca...\n\nClavelitos, clavelitos,\nclavelitos de mi corazón,\nyo te traigo clavelitos\ncolorados igual que un tizón.`
    },
    {
      title: 'Fonseca (Triste y Sola)',
      album: 'Himnos de Ronda Estudiantil',
      duration: '3:15',
      durationSec: 195,
      notes: [392, 440, 523, 587, 659, 523, 440, 392],
      lyrics: `Triste y sola, sola se queda Fonseca,\ntriste y llorosa queda la Universidad,\ny los libros, los libros se quedan mudos,\nlos tunos marchan a la ciudad...\n\nAdiós villa de Almería,\nadiós colegio mayor,\nque ya repican campanas,\nanunciando el nuevo amor.`
    },
    {
      title: 'La Morena de mi Copla',
      album: 'Pasodobles de Oro',
      duration: '3:30',
      durationSec: 210,
      notes: [659, 587, 523, 494, 440, 494, 523, 587],
      lyrics: `Julio Romero de Torres pintó a la mujer morena,\ncon ojos de misterio y el alma llena de pena.\nPor las calles de Almería resuena la serenata,\nque los tunos con salero le cantan a la muchacha.`
    }
  ],

  currentIndex: 0,
  isPlaying: false,
  currentTimeSec: 0,
  timer: null,
  audioCtx: null,

  init() {
    this.renderTrack();
    this.renderPlaylist();
  },

  getAudioContext() {
    if (!this.audioCtx) {
      const AudioContext = window.AudioContext || window.webkitAudioContext;
      if (AudioContext) this.audioCtx = new AudioContext();
    }
    if (this.audioCtx && this.audioCtx.state === 'suspended') {
      this.audioCtx.resume();
    }
    return this.audioCtx;
  },

  playTone(freq, time) {
    try {
      const ctx = this.getAudioContext();
      if (!ctx) return;
      const osc = ctx.createOscillator();
      const gain = ctx.createGain();
      osc.type = 'triangle'; // sonido acústico suave similar a guitarra/laúd
      osc.frequency.setValueAtTime(freq, ctx.currentTime);
      gain.gain.setValueAtTime(0.12, ctx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 0.8);
      osc.connect(gain);
      gain.connect(ctx.destination);
      osc.start();
      osc.stop(ctx.currentTime + 0.85);
    } catch (e) {}
  },

  togglePlay() {
    if (this.isPlaying) {
      this.pause();
    } else {
      this.play();
    }
  },

  play() {
    this.isPlaying = true;
    this.getAudioContext();
    const btn = document.getElementById('player-play-btn');
    if (btn) btn.innerHTML = '❚❚';
    
    TunaApp.showToast(`Reproduciendo: «${this.tracks[this.currentIndex].title}»`);

    clearInterval(this.timer);
    this.timer = setInterval(() => {
      this.currentTimeSec++;
      const track = this.tracks[this.currentIndex];
      
      // Tocar arpegio musical simulado
      const noteIdx = this.currentTimeSec % track.notes.length;
      this.playTone(track.notes[noteIdx], 0.6);

      if (this.currentTimeSec >= track.durationSec) {
        this.next();
      } else {
        this.updateProgress();
      }
    }, 1000);
  },

  pause() {
    this.isPlaying = false;
    clearInterval(this.timer);
    const btn = document.getElementById('player-play-btn');
    if (btn) btn.innerHTML = '▶';
  },

  next() {
    this.currentIndex = (this.currentIndex + 1) % this.tracks.length;
    this.currentTimeSec = 0;
    this.renderTrack();
    if (this.isPlaying) this.play();
  },

  prev() {
    this.currentIndex = (this.currentIndex - 1 + this.tracks.length) % this.tracks.length;
    this.currentTimeSec = 0;
    this.renderTrack();
    if (this.isPlaying) this.play();
  },

  selectTrack(idx) {
    this.currentIndex = idx;
    this.currentTimeSec = 0;
    this.renderTrack();
    this.play();
  },

  updateProgress() {
    const track = this.tracks[this.currentIndex];
    const fill = document.getElementById('player-progress-fill');
    const currEl = document.getElementById('player-time-current');
    
    if (fill) {
      const pct = (this.currentTimeSec / track.durationSec) * 100;
      fill.style.width = pct + '%';
    }
    if (currEl) {
      const mins = Math.floor(this.currentTimeSec / 60);
      const secs = this.currentTimeSec % 60;
      currEl.textContent = `${mins}:${secs < 10 ? '0' : ''}${secs}`;
    }
  },

  renderTrack() {
    const track = this.tracks[this.currentIndex];
    const titleEl = document.getElementById('player-title');
    const albumEl = document.getElementById('player-album');
    const totalEl = document.getElementById('player-time-total');
    const lyricsEl = document.getElementById('player-lyrics');

    if (titleEl) titleEl.textContent = track.title;
    if (albumEl) albumEl.textContent = track.album;
    if (totalEl) totalEl.textContent = track.duration;
    if (lyricsEl) lyricsEl.textContent = track.lyrics;

    this.updateProgress();
    this.highlightPlaylist();
  },

  renderPlaylist() {
    const list = document.getElementById('player-playlist-list');
    if (!list) return;

    list.innerHTML = this.tracks.map((t, idx) => `
      <li class="playlist-item ${idx === this.currentIndex ? 'active' : ''}" onclick="TunaAudioPlayer.selectTrack(${idx})" style="display:flex; justify-content:space-between; align-items:center; padding:10px 14px; border-radius:6px; cursor:pointer; margin-bottom:6px; transition:background 0.15s; background:${idx === this.currentIndex ? 'rgba(197,155,63,0.18)' : 'var(--soft)'}; border:1px solid ${idx === this.currentIndex ? 'var(--gold)' : 'var(--line)'};">
        <div style="display:flex; align-items:center; gap:10px;">
          <span style="color:var(--gold); font-weight:bold;">${idx + 1}.</span>
          <div>
            <strong style="color:var(--ink); font-size:13.5px; display:block;">${t.title}</strong>
            <span style="font-size:11.5px; color:var(--muted);">${t.album}</span>
          </div>
        </div>
        <span style="font-size:12px; font-weight:600; color:var(--muted);">${t.duration}</span>
      </li>
    `).join('');
  },

  highlightPlaylist() {
    document.querySelectorAll('.playlist-item').forEach((item, idx) => {
      if (idx === this.currentIndex) {
        item.style.background = 'rgba(197,155,63,0.18)';
        item.style.borderColor = 'var(--gold)';
      } else {
        item.style.background = 'var(--soft)';
        item.style.borderColor = 'var(--line)';
      }
    });
  }
};

document.addEventListener('DOMContentLoaded', () => {
  if (document.getElementById('player-title')) {
    TunaAudioPlayer.init();
  }
});

