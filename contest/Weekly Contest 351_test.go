package contest

import "testing"

func Test_countBeautifulPairs(t *testing.T) {
	type args struct {
		nums []int
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{
			name: "",
			args: args{
				nums: []int{2, 5, 1, 4},
			},
			want: 5,
		},
		{
			name: "",
			args: args{
				nums: []int{11, 21, 12},
			},
			want: 2,
		},
		{
			name: "",
			args: args{
				nums: []int{756, 1324, 2419, 495, 106, 111, 1649, 1474, 2001, 1633, 273, 1804, 2102, 1782, 705, 1529, 1761, 1613, 111, 186, 412},
			},
			want: 183,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := countBeautifulPairs(tt.args.nums); got != tt.want {
				t.Errorf("countBeautifulPairs() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_numberOfGoodSubarraySplits(t *testing.T) {
	type args struct {
		nums []int
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{
			name: "",
			args: args{
				nums: []int{0, 1, 0, 0, 1},
			},
			want: 3,
		},
		{
			name: "",
			args: args{
				nums: []int{0, 1, 0},
			},
			want: 1,
		},
		{
			name: "",
			args: args{
				nums: []int{0, 1, 0, 0},
			},
			want: 1,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := numberOfGoodSubarraySplits(tt.args.nums); got != tt.want {
				t.Errorf("numberOfGoodSubarraySplits() = %v, want %v", got, tt.want)
			}
		})
	}
}
