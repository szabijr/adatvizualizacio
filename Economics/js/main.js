document.addEventListener('DOMContentLoaded', function() {
    loadMetrics();
    loadConclusions();
    initializeCharts();
});

function loadMetrics() {
    fetch('data/metrics.json')
        .then(response => response.json())
        .then(data => {
            const container = document.getElementById('metrics-container');
            container.innerHTML = `
                <div class="metric-card"><strong>Total Records</strong><span>${data.total_records}</span></div>
                <div class="metric-card"><strong>Date Range</strong><span>${data.start_date} - ${data.end_date}</span></div>
                <div class="metric-card"><strong>Stock Indexes</strong><span>${data.stock_indexes.join(', ')}</span></div>
                <div class="metric-card"><strong>Avg Daily Return</strong><span>${data.average_daily_return}%</span></div>
                <div class="metric-card"><strong>Max Unemployment</strong><span>${data.max_unemployment}%</span></div>
                <div class="metric-card"><strong>Avg Inflation</strong><span>${data.avg_inflation}%</span></div>
            `;
        });
}

function loadConclusions() {
    fetch('data/conclusions.json')
        .then(response => response.json())
        .then(data => {
            const container = document.getElementById('conclusions-container');
            container.innerHTML = data.map(item => 
                `<div class="conclusion-card"><p>${item}</p></div>`
            ).join('');
        });
}

function flipCard(card) {
    card.classList.toggle('flipped');
}

function initializeCharts() {
    Promise.all([
        fetch('data/regime_segmentation.json').then(r => r.json()),
        fetch('data/market_stress.json').then(r => r.json()),
        fetch('data/candlestick_dow_jones.json').then(r => r.json()),
        fetch('data/candlestick_s&p_500.json').then(r => r.json()),
        fetch('data/candlestick_nasdaq.json').then(r => r.json()),
        fetch('data/correlation_heatmap.json').then(r => r.json()),
        fetch('data/unemployment_vs_performance.json').then(r => r.json()),
        fetch('data/inflation_vs_returns.json').then(r => r.json()),
        fetch('data/gdp_vs_performance.json').then(r => r.json()),
        fetch('data/volume_vs_price.json').then(r => r.json()),
        fetch('data/daily_volatility.json').then(r => r.json()),
        fetch('data/stock_trends.json').then(r => r.json())
    ]).then(([regimeData, stressData, dowData, spData, nasdaqData, corrData, unempData, inflData, gdpData, volData, volData2, trendData]) => {
        createRegimeChart(regimeData);
        createStressChart(stressData);
        createCandlestickChart(dowData, 'dowCandlestick', 'Dow Jones');
        createCandlestickChart(spData, 'spCandlestick', 'S&P 500');
        createCandlestickChart(nasdaqData, 'nasdaqCandlestick', 'NASDAQ');
        createHeatmap(corrData);
        createScatterChart(unempData, 'unemploymentChart', 'Unemployment Rate (%)', 'Close Price', '#ff6b6b');
        createScatterChart(inflData, 'inflationChart', 'Inflation Rate (%)', 'Daily Returns (%)', '#4ecdc4');
        createScatterChart(gdpData, 'gdpChart', 'GDP Growth (%)', 'Close Price', '#45b7d1');
        createScatterChart(volData, 'volumeChart', 'Trading Volume', 'Close Price', '#96ceb4');
        createVolatilityChart(volData2);
        createTrendsChart(trendData);
    });
}

function createRegimeChart(data) {
    const ctx = document.getElementById('regimeChart').getContext('2d');
    new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: Object.keys(data),
            datasets: [{
                data: Object.values(data),
                backgroundColor: ['#008080', '#006666', '#009999', '#00aaaa'],
                borderColor: '#1a1a2e',
                borderWidth: 2
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: { position: 'bottom', labels: { color: '#e0e0e0' } }
            }
        }
    });
}

function createStressChart(data) {
    const ctx = document.getElementById('stressChart').getContext('2d');
    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: data.stress_periods,
            datasets: [{
                label: 'Stress Periods Count',
                data: data.volatility_avg,
                backgroundColor: '#ff6b6b',
                borderColor: '#ff4444',
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            scales: {
                y: { ticks: { color: '#e0e0e0' }, grid: { color: '#333' } },
                x: { ticks: { color: '#e0e0e0' }, grid: { color: '#333' } }
            },
            plugins: {
                legend: { labels: { color: '#e0e0e0' } }
            }
        }
    });
}

function createCandlestickChart(data, canvasId, title) {
    const ctx = document.getElementById(canvasId).getContext('2d');
    const candleData = data.dates.map((date, i) => ({
        x: date,
        o: data.open[i],
        h: data.high[i],
        l: data.low[i],
        c: data.close[i]
    }));
    
    new Chart(ctx, {
        type: 'candlestick',
        data: {
            datasets: [{
                label: title,
                data: candleData
            }]
        },
        options: {
            responsive: true,
            scales: {
                y: { ticks: { color: '#e0e0e0' } },
                x: { ticks: { color: '#e0e0e0' } }
            },
            plugins: {
                legend: { labels: { color: '#e0e0e0' } }
            }
        }
    });
}

function createHeatmap(data) {
    const ctx = document.getElementById('heatmapChart').getContext('2d');
    const matrix = data.matrix;
    const labels = data.variables;
    
    const colors = matrix.map(row => 
        row.map(val => val > 0 ? 
            `rgba(0, 212, 212, ${Math.abs(val)})` : 
            `rgba(255, 107, 107, ${Math.abs(val)})`)
    );
    
    new Chart(ctx, {
        type: 'matrix',
        data: {
            labels: labels,
            datasets: [{
                data: colors.flat(),
                backgroundColor: colors.flat()
            }]
        },
        options: {
            responsive: true,
            scales: {
                y: { ticks: { color: '#e0e0e0' } },
                x: { ticks: { color: '#e0e0e0' } }
            }
        }
    });
}

function createScatterChart(data, canvasId, labelX, labelY, color) {
    const ctx = document.getElementById(canvasId).getContext('2d');
    
    const sampleSize = 200;
    const step = Math.ceil(data.dates.length / sampleSize);
    const sampledData = data.dates.filter((_, i) => i % step === 0).map((date, i) => ({
        x: data[labelX.toLowerCase().replace(' (%)', '').replace(' ', '_')][i * step],
        y: data[labelY.toLowerCase().replace(' (%)', '').replace(' ', '_')][i * step]
    }));
    
    new Chart(ctx, {
        type: 'scatter',
        data: {
            datasets: [{
                label: `${labelX} vs ${labelY}`,
                data: sampledData,
                backgroundColor: color + '80',
                borderColor: color
            }]
        },
        options: {
            responsive: true,
            scales: {
                x: { ticks: { color: '#e0e0e0' }, grid: { color: '#333' } },
                y: { ticks: { color: '#e0e0e0' }, grid: { color: '#333' } }
            },
            plugins: {
                legend: { labels: { color: '#e0e0e0' } }
            }
        }
    });
}

function createVolatilityChart(data) {
    const ctx = document.getElementById('volatilityChart').getContext('2d');
    
    const sampleSize = 100;
    const step = Math.ceil(data.dates.length / sampleSize);
    const volatilityData = data.dates.filter((_, i) => i % step === 0).map((date, i) => ({
        x: date,
        y: data.volatility[i * step]
    }));
    
    new Chart(ctx, {
        type: 'line',
        data: {
            datasets: [{
                label: 'Daily Volatility',
                data: volatilityData,
                borderColor: '#ffd93d',
                backgroundColor: 'rgba(255, 217, 61, 0.1)',
                fill: true,
                tension: 0.3
            }]
        },
        options: {
            responsive: true,
            scales: {
                x: { ticks: { color: '#e0e0e0' } },
                y: { ticks: { color: '#e0e0e0' }, grid: { color: '#333' } }
            },
            plugins: {
                legend: { labels: { color: '#e0e0e0' } }
            }
        }
    });
}

function createTrendsChart(data) {
    const ctx = document.getElementById('trendsChart').getContext('2d');
    
    const datasets = Object.entries(data).map(([name, d], i) => {
        const colors = ['#008080', '#006666', '#00d4d4'];
        return {
            label: name,
            data: d.dates.map((date, j) => ({ x: date, y: d.close[j] })),
            borderColor: colors[i],
            backgroundColor: colors[i] + '20',
            borderWidth: 2,
            pointRadius: 0,
            fill: false
        };
    });
    
    new Chart(ctx, {
        type: 'line',
        data: { datasets },
        options: {
            responsive: true,
            scales: {
                x: { ticks: { color: '#e0e0e0' } },
                y: { ticks: { color: '#e0e0e0' }, grid: { color: '#333' } }
            },
            plugins: {
                legend: { labels: { color: '#e0e0e0' } }
            }
        }
    });
}