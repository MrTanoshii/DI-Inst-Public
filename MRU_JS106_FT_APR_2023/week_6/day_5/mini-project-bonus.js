var options = {
  series: [
    {
      data: [],
    },
  ],
  chart: {
    height: 350,
    type: "rangeBar",
  },
  plotOptions: {
    bar: {
      horizontal: true,
      distributed: true,
      dataLabels: {
        hideOverflowingLabels: false,
      },
    },
  },
  dataLabels: {
    enabled: true,
    formatter: function (val, opts) {
      var label = opts.w.globals.labels[opts.dataPointIndex];
      var a = moment(val[0]);
      var b = moment(val[1]);
      var diff = b.diff(a, "days");
      return label + ": " + diff + (diff > 1 ? " days" : " day");
    },
    style: {
      colors: ["#f3f4f5", "#fff"],
    },
  },
  xaxis: {
    type: "datetime",
  },
  yaxis: {
    show: false,
  },
  theme: {
    mode: "dark",
  },
};
colors = [
  "#D7263D",
  "#662E9B",
  "#5C4742",
  "#3f51b5",
  "#546E7A",
  "#EA3546",
  "#2E294E",
  "#662E9B",
];

task_list.forEach((task, index) => {
  options.series[0].data.push({
    x: task.name + " | " + task.description,
    y: [Date.parse(task.start_date), Date.parse(task.end_date)],
    fillColor: colors[Math.floor(Math.random() * colors.length)],
  });
});

var chart = new ApexCharts(document.querySelector("#chart"), options);
chart.render();
